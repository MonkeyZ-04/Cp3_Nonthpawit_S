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
    select_currency = (input("Currency do u want : ")).upper()
    convert_currency = (input("Convert with : ")).upper()
    year_start = int(input("Year: "))
    month_start = int(input("month: "))
    day_start = int(input("date: "))
    year_end = int(input("Year: "))
    month_end = int(input("month: "))
    day_end = int(input("date: ")) + 1
    start_date = date(year_start, month_start, day_start)
    end_date = date(year_end, month_end, day_end)
    numbers = 0
    for single_date in daterange(start_date, end_date):
        date_obj = datetime.combine(single_date, datetime.min.time())
        value = c.get_rate(select_currency, convert_currency, date_obj)
        total = single_date.strftime('%Y-%m-%d:'), value
        numbers += value
        print(total)
    print("Average : ",numbers/(day_end-day_start))

def predict():
    select_currency = (input("Currency do u want : ")).upper()
    convert_currency = (input("Convert with : ")).upper()
    print("This process start at 1 mar 2021 cant predict year past")
    print("Available from 1 March 2021  onwards")
    select_mont = int(input("month: "))
    select_date = int(input("date: ")) + 1

    c = CurrencyRates()

    start_date = date(2021, 3, 1)
    end_date = date(2021, select_mont, select_date)
    numbers = 0
    value = 0

    for single_date in daterange(start_date, end_date):
        date_obj = datetime.combine(single_date, datetime.min.time())
        value = c.get_rate(select_currency, convert_currency, date_obj)
        numbers += value
    avr = numbers / (select_date - 1)
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


