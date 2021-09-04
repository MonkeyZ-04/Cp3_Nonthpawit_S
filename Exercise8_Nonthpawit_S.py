usernaemInput = input("Username : ")
passwordInput = input("Password : ")
if usernaemInput == "Customer" and passwordInput == "1234":
    print("Wellcome to OnlineShop")
    print("---------shop-----------")
    print("product list")
    print("1. Banana : 10 (THB)")
    print("2. Tomato : 8  (THB)")
    print("3. Water  : 5  (THB)")
    print("4. Egg    : 2  (THB)")
    userSelected = int(input("select>>>  "))
    if userSelected == 1:
        price = int(input("How many Bananas do you need? :  "))
        amout = print("The total price =" , price * 10,"THB")
    elif userSelected == 2:
        price = int(input("How many Tomatoes do you need? :  "))
        amout = print("The total price =" , price * 8,"THB")
    elif userSelected == 3:
        price = int(input("How many bottles of water do you need? :  "))
        amout = print("The total price =" , price * 5,"THB")
    elif userSelected == 4:
        price = int(input("How many Eggs do you need? :  "))
        amout = print("The total price =" , price * 2,"THB")
else :
    print("!!Pls Login agian!!")
