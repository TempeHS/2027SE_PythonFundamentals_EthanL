list = {}

while True:
    try:
        item = input().strip().upper()
    except EOFError:
        break

    if item == "":
        continue

    if item in list:
        list[item] += 1
    else:
        list[item] = 1

for item in sorted(list):
    print(f"{list[item]} {item}")
