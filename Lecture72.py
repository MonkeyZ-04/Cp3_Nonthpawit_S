menuList = []
def showBill():
    print("---- My Food----")
    total = 0
    for number in range(len(menuList)):
        print(menuList[number])#[0]ลำดับ0 ของlistแรก
        total += int(menuList[number][1])
    print("Total : ",total)
while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName, menuPrice])

showBill()