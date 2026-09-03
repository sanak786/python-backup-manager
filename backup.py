import os
import shutil
from datetime import datetime

SOURCE_DIR = "data_to_backup"
BACKUP_DIR = "backups"
MAX_BACKUPS = 3  # Sirf latest 3 backups safe rahenge, baki auto-delete

def create_backup():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    # Naya backup banana
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archive_name = f"backup_{timestamp}"
    destination_path = os.path.join(BACKUP_DIR, archive_name)

    print(f"Creating backup for '{SOURCE_DIR}'...")
    created_file = shutil.make_archive(destination_path, 'zip', SOURCE_DIR)
    print(f"Backup created: {created_file}")

    # Purane backups delete karne ka auto-cleanup logic
    clean_old_backups()

def clean_old_backups():
    # Saari zip files ki list date-wise sort karna
    files = [os.path.join(BACKUP_DIR, f) for f in os.listdir(BACKUP_DIR) if f.endswith('.zip')]
    files.sort(key=os.path.getmtime)

    # Agar files MAX_BACKUPS se zyada ho jayein toh sabse purani delete kar do
    while len(files) > MAX_BACKUPS:
        oldest_file = files.pop(0)
        os.remove(oldest_file)
        print(f"Retention policy: Deleted old backup -> {oldest_file}")

if __name__ == "__main__":
    create_backup()