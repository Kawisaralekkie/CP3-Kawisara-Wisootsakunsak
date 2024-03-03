print("Online Supermarket")
UserNameInput=input("Username :")
PasswordInput=input("Password :")
if UserNameInput == "Kawisara" and PasswordInput == "1204":
    print("Welcome to supermartket")
    CocaCola=15
    IceCream = 40
    Lay = 20
    print("1. Coca Cola = 15 THB")
    print("2. Lay BBQ flavor = 20 THB")
    print("3. Ice Cream = 40 THB")
    ProductSelected=int(input("Please select product :"))
    Numberofproduct=int(input("Piece :"))
    if ProductSelected == 1:
        TotalPrice=CocaCola*Numberofproduct
        print("Total price :",TotalPrice,"THB")
    elif ProductSelected == 2:
        TotalPrice = Lay* Numberofproduct
        print("Total price :", TotalPrice, "THB")
    elif ProductSelected == 3:
        TotalPrice = IceCream * Numberofproduct
print("-----------Thank You -------------")
