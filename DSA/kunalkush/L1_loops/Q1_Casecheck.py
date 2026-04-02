


def case_check(ch):
    if ord('a') <= ord(ch) <= ord('z'):
        print("lowercase")
    elif ord('A') <= ord(ch) <= ord('Z'):
        print("uppercase")
    else:
        print("not a character")

case_check('a')