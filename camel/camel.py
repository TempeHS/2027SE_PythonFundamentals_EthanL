user_input = input("input ")
u_input = ""

for char in user_input:
    if char.isupper():
        u_input += "_" + char.lower()
    else:
        u_input += char

print(u_input)
