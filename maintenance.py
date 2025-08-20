import os
import subprocess
import shutil
from datetime import datetime

# ===== CONFIG =====
REPO_PATH = r"C:\path\to\bpr-integration"  # ganti sesuai path kamu
LOGS_PATH = os.path.join(REPO_PATH, "logs")
BACKUP_PATH = os.path.join(REPO_PATH, "backup_logs")

# Daily / Harian
def daily_check():
    print("=== DAILY CHECK START ===")
    os.chdir(REPO_PATH)

    # Pull update
    subprocess.run(["git", "pull", "origin", "main"])

    # Run demo transactions
    demo_script = os.path.join(REPO_PATH, "src", "tests", "run_demo_full.py")
    if os.path.exists(demo_script):
        subprocess.run(["python", demo_script])
    else:
        print("Demo script not found!")

    # Check logs folder
    if os.path.exists(LOGS_PATH):
        log_files = os.listdir(LOGS_PATH)
        print(f"Found {len(log_files)} log files.")
    else:
        print("Logs folder not found!")

    # Git commit & push
    subprocess.run(["git", "add", "."])
    today = datetime.now().strftime("%Y-%m-%d")
    subprocess.run(["git", "commit", "-m", f"Daily update {today}"])
    subprocess.run(["git", "push", "origin", "main"])
    print("=== DAILY CHECK END ===\n")

# Weekly / Mingguan
def weekly_backup():
    print("=== WEEKLY BACKUP START ===")
    if not os.path.exists(BACKUP_PATH):
        os.makedirs(BACKUP_PATH)

    # Copy logs to backup folder with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder = os.path.join(BACKUP_PATH, f"logs_backup_{timestamp}")
    shutil.copytree(LOGS_PATH, backup_folder)
    print(f"Logs backed up to {backup_folder}")

    # Git commit & push backup summary
    os.chdir(REPO_PATH)
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"Weekly backup {timestamp}"])
    subprocess.run(["git", "push", "origin", "main"])
    print("=== WEEKLY BACKUP END ===\n")

# ===== MAIN =====
if __name__ == "__main__":
    print("Select maintenance type:")
    print("1. Daily check")
    print("2. Weekly backup")
    choice = input("Enter 1 or 2: ").strip()
    if choice == "1":
        daily_check()
    elif choice == "2":
        weekly_backup()
    else:
        print("Invalid choice!")
