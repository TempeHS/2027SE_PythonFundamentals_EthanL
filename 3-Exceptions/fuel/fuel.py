while True:
    try:
        fraction = input("Fraction: ").strip()
        x_str, y_str = fraction.split("/")
        x = int(x_str)
        y = int(y_str)

        if y != 4 or x > y or x < 0:
            raise ValueError

        percentage = round((x / y) * 100)

        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")
        break
    except (ValueError, ZeroDivisionError):
        pass
