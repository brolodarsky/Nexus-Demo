---
aliases: [Dad's Laptop Backup, Robocopy Backup, Easy Backup Script]
tags: [family, backup, automation, logistics]
type: tool
---
**Back to:** [[Table of Contents]]

---

### Description
This protocol defines a "software-only" backup method for Dad’s laptop using **Robocopy**, a powerful tool built directly into Windows. This eliminates the need to install third-party software like FreeFileSync on his machine.

---

### Step 1: Identify Backup Scope
Decide which folders need to be backed up. Common targets include:
*   `C:\Users\Dad\Documents`
*   `C:\Users\Dad\Pictures`
*   `C:\Users\Dad\Desktop`

---

### Step 2: Create the Backup Script
You can create a simple `.bat` file that he can double-click to run the backup.

1.  Open Notepad.
2.  Paste the following code (adjust the drive letter `D:` to match his external drive):

```batch
@echo off
echo Starting Dad's Laptop Backup...
echo ---------------------------------

:: Mirror Desktop
robocopy "C:\Users\gems1\Desktop" "D:\LV Comp Backup\Desktop" /MIR /FFT /R:3 /W:5 /Z /NP /LOG:"D:\LV Comp Backup\backup_log.txt"

:: Mirror Documents
robocopy "C:\Users\gems1\Documents" "D:\LV Comp Backup\Documents" /MIR /FFT /R:3 /W:5 /Z /NP /LOG:"D:\LV Comp Backup\backup_log.txt"

:: Mirror Downloads
robocopy "C:\Users\gems1\Downloads" "D:\LV Comp Backup\Downloads" /MIR /FFT /R:3 /W:5 /Z /NP /LOG:"D:\LV Comp Backup\backup_log.txt"

:: Mirror Pictures
robocopy "C:\Users\gems1\Pictures" "D:\LV Comp Backup\Pictures" /MIR /FFT /R:3 /W:5 /Z /NP /LOG:"D:\LV Comp Backup\backup_log.txt"

:: Mirror Videos
robocopy "C:\Users\gems1\Videos" "D:\LV Comp Backup\Videos" /MIR /FFT /R:3 /W:5 /Z /NP /LOG:"D:\LV Comp Backup\backup_log.txt"

echo ---------------------------------
echo Backup Complete!
pause
```

3.  Save the file as `Run_Backup.bat` directly on his desktop or on the root of the external drive.

---

### Step 3: Execution Procedure
1.  **Connect Drive:** Plug the external backup drive into his laptop.
2.  **Run Script:** Double-click `Run_Backup.bat`. 
3.  **Monitor:** A command window will show the progress. It will say "Press any key to continue" when finished.
4.  **Verify:** Check the `backup_log.txt` on the external drive for any "FAILED" entries.

---

### Comparison: Why Robocopy?
| Feature | Robocopy (Built-in) | FreeFileSync |
| :--- | :--- | :--- |
| **Installation** | None (Pre-installed) | Required (or Portable) |
| **Interface** | Command Line (Text) | GUI (Visual) |
| **Speed** | Extremely Fast | Fast |
| **Dad-Proofing** | One-click `.bat` file | Needs app navigation |

*Note: If you prefer the visual interface of FreeFileSync, you can use the **Portable Edition** by copying the program folder to the backup drive itself. This allows you to run it on his laptop without installing it.*

---

### Maintenance
Review the `backup_log.txt` once every few months to ensure no critical files are being skipped due to permission errors.
