from pathlib import Path

def parse_positive_int(value):
    try:
        number = int(value)
    except ValueError:
        return None
    if number > 0:
        return number
    return None


total = 0
count = 0

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "numbers.txt"

with file_path.open() as f:
    for line in f:
        value = line.strip()
        number = parse_positive_int(value)
        if number is not None:
            total += number
            count += 1

print("Sum:", total)
print("Count:", count)
