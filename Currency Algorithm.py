from datetime import datetime
from datetime import timedelta, date
from forex_python.converter import CurrencyRates


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def showmenu():
    print("Wellcome to Website")
    print("---------service-----------")
    print("1. Currency arverage")
    print("2. Predict Currency")
def menu_select():
    userSelected = int(input(">>> : "))
    return userSelected

def currency_arverage():
    c = CurrencyRates()
    x = int(input("Year: "))
    y = int(input("month: "))
    z = int(input("date: "))
    a = int(input("Year: "))
    b = int(input("month: "))
    d = int(input("date: ")) + 1
    start_date = date(x, y, z)
    end_date = date(a, b, d)
    numbers = 0
    for single_date in daterange(start_date, end_date):
        date_obj = datetime.combine(single_date, datetime.min.time())
        value = c.get_rate('USD', 'THB', date_obj)
        total = single_date.strftime('%Y-%m-%d:'), value
        numbers += value
        print(total)
    print("Average : ",numbers/(d-z))

def predict():
    print("This process start at 1 mar 2021 cant predict year past")
    print("Available from 1 March 2021  onwards")
    y = int(input("month: "))
    z = int(input("date: ")) + 1
    c = CurrencyRates()

    start_date = date(2021, 3, 1)
    end_date = date(2021, y, z)
    numbers = 0
    value = 0

    for single_date in daterange(start_date, end_date):
        date_obj = datetime.combine(single_date, datetime.min.time())
        value = c.get_rate('USD', 'THB', date_obj)
        numbers += value
    avr = numbers / (z - 1)
    per = abs(((avr*100 )/ value)-100)
    print("predict(percentage) :  +-", per)
    print("about               :+  ", (avr*(100+per))/100)
    print("                    :-  ", (avr*(100-per))/100)
showmenu()
print("Wellcome to Currency Program")
result = menu_select()
if result == 1:
    currency_arverage()
elif result == 2:
    predict()
else:
    print("Error")


