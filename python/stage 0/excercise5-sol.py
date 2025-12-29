def parse_positive_int(value):
    try:
        number = int(value)
    except ValueError:
        return None

    if number > 0:
        return number

    return None
