# import time
# import json
# import os

# metadata_table = {}

# METADATA_BACKUP_PATH = "backups/metadata_backup.json"

# def create_metadata(filename, size, blocks):
#     metadata_table[filename] = {
#         "name": filename,
#         "size": size,
#         "blocks": blocks,
#         "created": time.time(),
#         "modified": time.time(),
#         "accessed": time.time(),
#         "is_deleted": False
#     }

# def get_metadata(filename=None):
#     if filename:
#         return metadata_table.get(filename)
#     else:
#         return list(metadata_table.values())  # return all metadata as a list

# def mark_deleted(filename):
#     if filename in metadata_table:
#         metadata_table[filename]['is_deleted'] = True

# def save_metadata_backup():
#     with open(METADATA_BACKUP_PATH, "w") as f:
#         json.dump(metadata_table, f)
#     print("[Backup] Metadata backup saved.")

# def load_metadata_backup():
#     global metadata_table
#     if os.path.exists(METADATA_BACKUP_PATH):
#         with open(METADATA_BACKUP_PATH, "r") as f:
#             metadata_table = json.load(f)
#         print("[Recovery] Metadata loaded from backup.")
#     else:
#         print("[Recovery] No metadata backup found.")

# def update_metadata(name, new_data):
#     if name in metadata_table:
#         metadata_table[name] = new_data
#         print(f"[Update] Metadata for '{name}' updated.")
#     else:
#         print(f"[Error] File '{name}' not found in metadata.")

import time
import json
import os

# Global metadata table
metadata_table = {}

# Path for metadata backup
METADATA_BACKUP_PATH = "backups/metadata_backup.json"

# Create new metadata entry
def create_metadata(filename, size, blocks):
    metadata_table[filename] = {
        "name": filename,
        "size": size,
        "blocks": blocks,
        "created": time.time(),
        "modified": time.time(),
        "accessed": time.time(),
        "is_deleted": False
    }

# Get single file metadata or full metadata table
def get_metadata(filename=None):
    if filename:
        return metadata_table.get(filename)
    else:
        return metadata_table  # Return full dictionary for backup/undelete

# Mark a file as deleted
def mark_deleted(filename):
    if filename in metadata_table:
        metadata_table[filename]['is_deleted'] = True
        metadata_table[filename]['modified'] = time.time()
    else:
        print(f"[Error] File '{filename}' not found.")

# Save metadata table to backup file
def save_metadata_backup():
    with open(METADATA_BACKUP_PATH, "w") as f:
        json.dump(metadata_table, f, indent=4)
    print("[Backup] Metadata backup saved.")

# Load metadata from backup file
def load_metadata_backup():
    global metadata_table
    if os.path.exists(METADATA_BACKUP_PATH):
        with open(METADATA_BACKUP_PATH, "r") as f:
            metadata_table = json.load(f)
        print("[Recovery] Metadata loaded from backup.")
    else:
        print("[Recovery] No metadata backup found.")

# Update metadata for a file
def update_metadata(name, new_data):
    if isinstance(new_data, dict):
        metadata_table[name] = new_data
        print(f"[Update] Metadata for '{name}' updated.")
    else:
        print(f"[Error] Invalid data format for '{name}'.")
