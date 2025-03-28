# from file_system.metadata import create_metadata, get_metadata, mark_deleted
# from file_system.allocator import allocate_blocks, defragment
# from file_system.disk import write_block, read_block, disk
# from file_system.journal import log_operation, replay_journal
# from file_system.compression import compress, decompress
# from file_system.recovery import undelete, save_metadata_backup
# from file_system.cache import file_cache



# def run_cli():
#     while True:
#         cmd = input("FS> ").split()
#         if not cmd: continue

#         if cmd[0] == "create":
#             name, size = cmd[1], int(cmd[2])
#             blocks = allocate_blocks(size)
#             if not blocks:
#                 print("Not enough space.")
#                 continue
#             create_metadata(name, size, blocks)
#             log_operation("CREATE", name)
#             print(f"File '{name}' created.")

#         elif cmd[0] == "write":
#             name, data = cmd[1], " ".join(cmd[2:])
#             meta = get_metadata(name)
#             if not meta or meta["is_deleted"]:
#                 print("File not found.")
#                 continue
#             data = compress(data)
#             for i, block in enumerate(meta["blocks"]):
#                 write_block(block, data[i * 64:(i+1) * 64])
#             file_cache.put(name, data)
#             log_operation("WRITE", name)
#             print("Data written.")

#         elif cmd[0] == "read":
#             name = cmd[1]
#             meta = get_metadata(name)
#             if not meta or meta["is_deleted"]:
#                 print("File not found.")
#                 continue
#             if file_cache.get(name):
#                 print("Cache:", decompress(file_cache.get(name)))
#             else:
#                 data = ""
#                 for block in meta["blocks"]:
#                     data += read_block(block) or ""
#                 print("Disk:", decompress(data))

#         elif cmd[0] == "delete":
#             name = cmd[1]
#             mark_deleted(name)
#             log_operation("DELETE", name)
#             print(f"'{name}' marked as deleted.")

#         elif cmd[0] == "undelete":
#             if undelete(cmd[1]):
#                 print("File recovered.")
#             else:
#                 print("Recovery failed.")

#         elif cmd[0] == "backup":
#             save_metadata_backup()
#             print("Metadata backed up.")

#         elif cmd[0] == "defrag":
#             defragment(disk)
#             print("Disk defragmented.")

#         elif cmd[0] == "replay":
#             replay_journal()

#         elif cmd[0] == "exit":
#             break

#         else:
#             print("Unknown command.")



from file_system.metadata import create_metadata, get_metadata, mark_deleted
from file_system.allocator import allocate_blocks
from file_system.disk import write_block, read_block, disk
from file_system.journal import log_operation, replay_journal
from file_system.compression import compress, decompress
from file_system.recovery import undelete, save_metadata_backup
from file_system.cache import file_cache
from file_system.optimizer import defragment  # Make sure this is correctly defined


def run_cli():
    while True:
        cmd = input("FS> ").strip().split()
        if not cmd:
            continue

        command = cmd[0].lower()

        if command == "create" and len(cmd) == 3:
            name, size = cmd[1], int(cmd[2])
            blocks = allocate_blocks(size)
            if not blocks:
            ommand == "write" and len(cmd) >= 3:
            name, data = cmd[1], " ".join(cmd[2:])
            meta = get_metadata(name)
            if not meta or meta["is_deleted"]:
                print("[Error] File not found or deleted.")
                  print("Not enough space.")
                continue
            create_metadata(name, size, blocks)
            log_operation("CREATE", name)
            print(f"[Create] File '{name}' created.")

        elif c  continue
            data = compress(data)
            for i, block in enumerate(meta["blocks"]):
                write_block(block, data[i * 64:(i + 1) * 64])
            file_cache.put(name, data)
            log_operation("WRITE", name)
            print("[Write] Data written to file.")

        elif command == "read" and len(cmd) == 2:
            name = cmd[1]
            meta = get_metadata(name)
            if not meta or meta["is_deleted"]:
                print("[Error] File not found or deleted.")
                continue
            cached = file_cache.get(name)
            if cached:
                print("[Cache]", decompress(cached))
            else:
                data = ""
                for block in meta["blocks"]:
                    data += read_block(block) or ""
                print("[Disk]", decompress(data))

        elif command == "delete" and len(cmd) == 2:
            name = cmd[1]
            mark_deleted(name)
            log_operation("DELETE", name)
            print(f"[Delete] File '{name}' marked as deleted.")

        elif command == "undelete" and len(cmd) == 2:
            if undelete(cmd[1]):
                print("[Recovery] File recovered.")
            else:
                print("[Recovery] Failed to recover file.")

        elif command == "backup":
            save_metadata_backup()

        elif command == "defragment" or command == "defrag":
            defragment()
            print("[Optimize] Disk defragmented.")

        elif command == "replay":
            replay_journal()

        elif command == "exit":
            break

        else:
            print("[Error] Unknown command.")
