# Lesson 1: Simple ReAct Agent from Scratch
# based on https://til.simonwillison.net/llms/python-react-pattern

import re
from dotenv import load_dotenv

# Load environment variables (like OPENAI_API_KEY) from .env file
_ = load_dotenv()
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

class Agent:
    """
    A simple wrapper for the OpenAI Chat Completions API that maintains state (message history).
    This allows the LLM to 'remember' previous thoughts and observations in a multi-turn conversation.
    """
    def __init__(self, systemPrompt=""):
        self.systemPrompt = systemPrompt
        self.messages = []
        if self.systemPrompt:
            # The system prompt defines the Agent's "persona" and rules (the ReAct logic)
            self.messages.append({"role": "system", "content": systemPrompt})

    def __call__(self, message):
        """Allows the agent instance to be called like a function: abot('message')"""
        self.messages.append({"role": "user", "content": message})
        result = self.execute()
        self.messages.append({"role": "assistant", "content": result})
        return result

    def execute(self):
        """Sends the current message history to the LLM and returns the response."""
        completion = client.chat.completions.create(
                        model="gpt-4o-mini", 
                        temperature=0, # Temperature 0 ensures deterministic/consistent reasoning
                        messages=self.messages)
        return completion.choices[0].message.content

# The ReAct Prompt: This is the 'source code' for the agent's reasoning process.
# It explicitly tells the LLM to follow a specific loop:
# 1. Thought: Reason about what to do next.
# 2. Action: Call a tool and immediately stop (PAUSE).
# 3. Observation: The script will then provide the result of that tool.
# 4. Answer: Final response once enough info is gathered.
systemPrompt = """
You run in a loop of Thought, Action, PAUSE, Observation.
At the end of the loop you output an Answer
Use Thought to describe your thoughts about the question you have been asked.
Use Action to run one of the actions available to you - then return PAUSE.
Observation will be the result of running those actions.

Your available actions are:

calculate:
e.g. calculate: 4 * 7 / 3
Runs a calculation and returns the number - uses Python so be sure to use floating point syntax if necessary

average_dog_weight:
e.g. average_dog_weight: Collie
returns average weight of a dog when given the breed

Example session:

Question: How much does a Bulldog weigh?
Thought: I should look the dogs weight using average_dog_weight
Action: average_dog_weight: Bulldog
PAUSE

You will be called again with this:

Observation: A Bulldog weighs 51 lbs

You then output:

Answer: A bulldog weighs 51 lbs
""".strip()


# Tool definitions: These are the functions the agent can "call"
def calculate(what):
    """Executes a mathematical expression using Python's eval."""
    return eval(what)

def average_dog_weight(name):
    """A mock database returning average weights for specific dog breeds."""
    if name in "Scottish Terrier": 
        return("Scottish Terriers average 20 lbs")
    elif name in "Border Collie":
        return("a Border Collies average weight is 37 lbs")
    elif name in "Toy Poodle":
        return("a toy poodles average weight is 7 lbs")
    else:
        return("An average dog weights 50 lbs")

# Mapping the names found in the prompt to the actual Python functions
known_actions = {
    "calculate": calculate,
    "average_dog_weight": average_dog_weight
}


# --- MANUAL REACT DEMONSTRATION ---
# This section shows how we manually 'feed' the agent observations step-by-step.

print("--- MANUAL REACT DEMONSTRATION ---")
print("This section shows how we manually 'feed' the agent observations step-by-step.")
print("\n")

abot = Agent(systemPrompt)

# First call: The agent doesn't know the answer yet, so it should output a Thought and an Action.
result = abot("How much does a toy poodle weigh?")
print("User: How much does a toy poodle weigh?")
print("Step 1: The agent doesn't know the answer yet, so it should output a Thought and an Action.")
print("Agent: ", result)
print("\n")

# Manually running the tool the agent requested
result = average_dog_weight("Toy Poodle")
print("Step 2: Manually running the tool the agent requested")
print("Manual result: ", result)
print("\n")

# Formatting the tool output as an 'Observation' to feed back into the agent
next_prompt = "Observation: {}".format(result)
print("Step 3: Formatting the tool output as an 'Observation' to feed back into the agent")
print("Next prompt to feed: ", next_prompt)
print("\n")

# The agent now takes the observation and should arrive at the Answer.
abot(next_prompt)
print("Step 4: The agent now takes the observation and should arrive at the Answer.")
print("Agent: ", abot.messages[-1]["content"])
print("\n")

# Checking the message history to see how the 'state' grew
print("Step 5: Checking the message history to see how the 'state' grew")
print("Agent: ")
for message in abot.messages:
    print(message, "\n")
print("\n")

# --- AUTOMATED REACT LOOP ---

# Regex to find 'Action: method: input' in the LLM's response
# Note: Using a raw string r'' to avoid Python's SyntaxWarning for '\w'

print("--- AUTOMATED REACT LOOP ---")
print("This section shows how we automatically 'feed' the agent observations step-by-step.")
print("\n")

# Regex to find 'Action: method: input' in the LLM's response
# It works by looking for the word 'Action' followed by a colon, then capturing the method name and arguments.
# Note: Using a raw string r'' to avoid Python's SyntaxWarning for '\w'
action_re = re.compile(r'^Action: (\w+): (.*)$')   

def query(question, max_turns=5):
    """
    Automates the ReAct loop:
    1. Sends the question to the Agent.
    2. Checks if the response contains an 'Action'.
    3. If yes, runs the tool, gets the 'Observation', and loops back.
    4. If no, assumes the agent has reached an 'Answer' and finishes.
    """
    i = 0
    bot = Agent(systemPrompt)
    next_prompt = question
    while i < max_turns:
        i += 1
        result = bot(next_prompt)
        print("Agent: ", result)
        print("\n")
        
        # Look for actions in the current turn's output
        actions = [
            action_re.match(a) # a is a line in the result
            for a in result.split('\n') 
            if action_re.match(a)
        ]
        
        if actions:
            # The LLM wants to take an action. Extract the function name and arguments.
            action, action_input = actions[0].groups()
            if action not in known_actions:
                raise Exception("Unknown action: {}: {}".format(action, action_input))
            
            print(" -- running {} {}".format(action, action_input))
            # Execute the function
            observation = known_actions[action](action_input)
            print("Observation:", observation)
            print("\n")
            
            # Prepare the observation to be the next input for the agent in the next iteration
            next_prompt = "Observation: {}".format(observation)
        else:
            # No action found, which usually means the LLM provided an 'Answer'
            return

# Testing the automated loop with a complex multi-step question
question = """I have 2 dogs, a border collie and a scottish terrier. \
What is their combined weight"""
query(question)

