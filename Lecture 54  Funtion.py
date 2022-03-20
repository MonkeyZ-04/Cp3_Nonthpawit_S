""""
def vatCalculate(totalPrince = float(input("Total Prince :  "))):
    return totalPrince+(totalPrince*7/100)
print(vatCalculate())
"""
def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("Success")
        return True
    else:
        print("Pls try again")
        return False
def Showmenu():
    print("Wellcome to Website")
    print("---------shop-----------")
    print("1. vat Calculator")
    print("2. Prince Calculator")
def manuSelect():
    userSelected = int(input(">>>"))
    return userSelected
def vatCalculate(totalprince):
    vat = 7
    result = totalprince + totalprince * vat / 100
    print(result)
def princeCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

if login():
    Showmenu()
    print("Hello world")
    print(Showmenu())
    result = manuSelect()
    if result == 1:
        totalprince = int(input("Total price :"))
        vat = 7
        result2 = totalprince + totalprince * vat / 100
        print(result2)
    elif result ==2:
        print(princeCalculate())



#login
#show manu
#select menu
#vat