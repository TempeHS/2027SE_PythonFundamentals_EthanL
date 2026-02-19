user_input = input("What is your question? ")
x, y, z = user_input.strip(" ")
x = float(x)
z = float(z)
if y == "+":
    result = x + z
print(result)
