total = 0

while True:
    value = input("Enter a number (or 'done'): ")

    if value == "done":
        break

    total = total + int(value)

print("Total:", total)
