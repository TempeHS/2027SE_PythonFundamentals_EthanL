user_input = input("Enter file ").strip().lower()
if user_input.endswith(".jpg"):
    print("photo/png")
elif user_input.endswith(".pdf"):
    print("application.pdf")
else:
    print("File type unrecognized")
