BLOCK_SIZE = 64
TOTAL_BLOCKS = 1000
disk = [None] * TOTAL_BLOCKS

def read_block(index):
    return disk[index]

def write_block(index, data):
    disk[index] = data[:BLOCK_SIZE]
