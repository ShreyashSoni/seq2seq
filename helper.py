import os


def load_data(path):
    input_file = os.path.join(path)
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        data = f.read()
        
    return data

