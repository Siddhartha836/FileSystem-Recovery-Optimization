def compress(data):
    return ''.join([c for i, c in enumerate(data) if i % 2 == 0])

def decompress(data):
    return ''.join([c + '_' for c in data])
