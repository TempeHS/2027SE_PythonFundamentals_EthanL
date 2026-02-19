def main():
    time = input("time ")
    c_time = convert(time)
    if c_time >= 7 and c_time <= 8:
        print("breakfast time")
    elif c_time >= 12 and c_time <= 13:
        print("dinner time:")
    elif c_time >= 18 and c_time <= 19:
        print("lunch time")
    else:
        print("nothing")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours) + (float(minutes) / 60)
    return hours


main()
