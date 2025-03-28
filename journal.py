import json
import os

journal_file = "file_system/journal.log"

# Function to log operations
def log_operation(operation, filename, data=None):
    entry = {
        "operation": operation,
        "filename": filename,
        "data": data
    }
    with open(journal_file, "a") as f:
        f.write(json.dumps(entry) + "\n")

# Function to replay operations from the journal
def replay_journal():
    if not os.path.exists(journal_file):
        return
    with open(journal_file, "r") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                print(f"Replaying: {entry}")
                # You could implement auto-recovery here using the entry
            except Exception as e:
                print(f"Error reading journal entry: {e}")
