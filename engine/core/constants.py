import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Paths
ENGINE_ROOT = Path(__file__).parent.parent
PROJECT_ROOT = ENGINE_ROOT.parent

VAULT_PATH = Path(os.getenv("VAULT_PATH", PROJECT_ROOT / "mock_vault"))

# AI Config
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AI_MODEL = "gpt-5.4-mini"

# Shared Config
IGNORE_DIRS = {
    "Audio",
    ".trash",
    ".obsidian",
    ".stfolder",
    ".vscode",
    "Memories_Log_Images",
    "Pilot Diagrams",
    "node_modules",
    "__pycache__",
    ".venv",
    ".git",
}
