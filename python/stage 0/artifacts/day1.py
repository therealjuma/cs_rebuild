p = input("P: True of False").strip()
q = input("Q: True of False").strip()

values_expected = ['true', 'false']

if p or q not in values_expected:
    print("input not expected")

if p == "true":
    if q == "true":
        print("Statement is TRUE")

    else:
        print("Statement is False")

else:
    if q == "false":
        print("Statement is True")

    else:
        print("Statement is False")



