
def str_to_binary(data):
    converted_data = data.encode('utf-8')
    return converted_data

def binary_to_str(data):
    converted_data = bytes(data).decode('utf-8')
    return converted_data
