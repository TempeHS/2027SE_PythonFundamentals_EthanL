coin_inserted = int(input("Insert coin: "))
if coin_inserted in [25, 10, 5]:
    remain = 50 - coin_inserted
    print("Amount due: ", remain)
    if remain != 0:
        Change_Owed = int(input("Insert coin: "))
        Final_remain = remain - Change_Owed
        print("Change Owed: ", Final_remain)
else:
    print("Amount Due 50")
