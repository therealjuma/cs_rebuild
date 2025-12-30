total = 0
count = 0

def parse_positive_int(value):
    try:
        number = int(value)
    except ValueError:
        return None

    if number > 0:
        return number

    return None

while True:
    value = input("Enter a positive integer (or 'done'): ")

    if value == "done":
        break

    number = parse_positive_int(value)

    if number is not None:
        total += number
        count += 1


print("Sum:", total)
print("Count:", count)
