p = input("P (true/false): ").strip().lower()
q = input("Q (true/false): ").strip().lower()

values_expected = ["true", "false"]

if p not in values_expected or q not in values_expected:
    print("Invalid input")
    exit()

if p == "true" and q == "false":
    print("Statement is FALSE")
else:
    print("Statement is TRUE")
