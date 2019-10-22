def list_convert_into_int(list):
    result = []
    for n in list:
        try:
            result.append(int(n))
        except Exception:
            pass
    return result
