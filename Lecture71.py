def showBill():
    print("-----Food-------")
    total = 0
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        total += int(priceList[number])
    print("Total : ",total)
menuList = []
priceList = []
while True:
    menuName = input("Please Enter Your menu : ")
    if(menuName.lower() == "x"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
print(menuList,priceList)
showBill()
