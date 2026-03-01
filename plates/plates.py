def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False
    seen_number = False
    for char in s:
        if char.isdigit():
            if not seen_number:
                if char == "0":
                    return False
                seen_number = True
        else:
            if seen_number:
                return False
    return True


main()
