total = 0
count = 0

while True:
    value = input("Enter a positive integer (or 'done'): ")

    if value == "done":
        break
    
    try:
        number = int(value)

        if number > 0:
            total += number
            count += 1

    except ValueError:
        print("Invalid input")

print("Sum:", total)
print("Count:", count)
