def convert_str_into_int(data):
    if type(data) is not list:
        return int(data)
    result = []
    for n in data:
        try:
            result.append(int(n))
        except Exception:
            pass
    return result
