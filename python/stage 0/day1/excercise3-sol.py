total = 0

while True:
    value = input("Enter a number (or 'done'): ")

    if value == "done":
        break

    try:
        total += int(value)
    except ValueError:
        print("Invalid input, ignored")

print("Total:", total)
