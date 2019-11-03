def list_to_dict(keys, values):
    if len(keys) != len(values):
        raise Exception("Keys and Values length not match")
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result