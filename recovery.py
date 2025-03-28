import os
import json
from file_system.metadata import metadata_table, update_metadata

BACKUP_PATH = "backups/metadata_backup.json"

# ✅ Save entire metadata table to backup
def save_metadata_backup():
    os.makedirs("backups", exist_ok=True)  # Ensure backup folder exists
    with open(BACKUP_PATH, "w") as f:
        json.dump(metadata_table, f)
    print("[Backup] Metadata backup saved.")

# ✅ Undelete a file from backup
def undelete(name):
    if not os.path.exists(BACKUP_PATH):
        print("[Error] No backup found.")
        return False

    with open(BACKUP_PATH, "r") as f:
        backup = json.load(f)

    if name in backup:
        from file_system.metadata import update_metadata
        update_metadata(name, backup[name])
        print(f"[Recovery] File '{name}' restored from backup.")
        return True

    print(f"[Recovery] File '{name}' not found in backup.")
    return False


# import os
# import json
# from file_system.metadata import metadata_table, update_metadata

# # Path to the metadata backup file
# BACKUP_PATH = "backups/metadata_backup.json"

# # ✅ Save the current metadata_table to a JSON backup
# def save_metadata_backup():
#     os.makedirs("backups", exist_ok=True)  # Ensure the backup folder exists
#     with open(BACKUP_PATH, "w") as f:
#         json.dump(metadata_table, f, indent=4)
#     print("[Backup] Metadata backup saved.")

# # ✅ Restore metadata for a specific file from backup
# def undelete(name):
#     if not os.path.exists(BACKUP_PATH):
#         print("[Error] No backup found.")
#         return False

#     with open(BACKUP_PATH, "r") as f:
#         backup = json.load(f)

#     if name in backup:
#         file_data = backup[name]
#         update_metadata(name, file_data)
#         print(f"[Recovery] File '{name}' restored from backup.")
#         return True

#     print(f"[Recovery] File '{name}' not found in backup.")
#     return False
