total = 0

while True:
    value = input("Enter a number (or 'done'): ")

    if value == "done":
        break

    else:
        print("Unexpected input")

    try:
        total += int(value)

    except ValueError:
        pass

print("Total:", total)
