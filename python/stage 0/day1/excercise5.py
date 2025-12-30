def parse_positive_int(value):

    try:
        if int(value) > 0:
            return int(value)

    except ValueError:
        return None


print(parse_positive_int("5"))    # → 5
print(parse_positive_int("-2"))    # → None
print(parse_positive_int("0"))   # → None
print(parse_positive_int("3.5"))   # → None
print(parse_positive_int("done"))  # → None
