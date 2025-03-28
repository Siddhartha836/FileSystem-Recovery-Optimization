from file_system.disk import disk
from file_system.metadata import get_metadata, update_metadata

disk_size = 1000
disk = [None] * disk_size

def allocate_blocks(size):
    free_blocks = [i for i, block in enumerate(disk) if block is None]
    if len(free_blocks) < size:
        return []
    return free_blocks[:size]

def defragment(disk):
    new_disk = [None] * len(disk)
    new_index = 0
    updated_files = []

    from file_system.metadata import get_metadata, update_metadata  # Local import to avoid circular import

    for i in range(len(disk)):
        if disk[i] is not None:
            new_disk[new_index] = disk[i]
            for file in get_metadata():
                if i in file["blocks"]:
                    file["blocks"] = [new_index if b == i else b for b in file["blocks"]]
                    updated_files.append(file)
            new_index += 1

    for file in updated_files:
        update_metadata(file["name"], file)

    disk[:] = new_disk
   
def free_blocks(blocks):
    from file_system.disk import disk
    for block in blocks:
        disk[block] = None
