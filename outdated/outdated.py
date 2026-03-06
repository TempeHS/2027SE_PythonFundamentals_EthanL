calendar = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}
while True:
    try:
        date = input("Date: ").title().strip()
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

            if not (1 <= month <= 12):
                continue

            print(f"{year}-{month}-{day}")
            break

        elif "," in date:
            month_day, year = date.split(",")
            month, day = month_day.split()
            year = int(year.strip())
            day = int(day)

            month = calendar[month]

            if not (1 <= day <= 31):
                continue

            print(f"{year}-{month}-{day}")
            break

    except (TypeError, ValueError, KeyError):
        continue
