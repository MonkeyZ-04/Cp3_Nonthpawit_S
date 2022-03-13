from tkinter import *
from datetime import datetime
from datetime import timedelta, date
from forex_python.converter import CurrencyRates

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def arverage_leftclickbutton(event):
    c = CurrencyRates()
    start_date = date(int(start_year_box.get()), int(start_month_box.get()), int(start_day_box.get()))
    end_date = date(int(end_year_box.get()), int(end_month_box.get()), (int(end_day_box.get())+1))
    numbers = 0
    for single_date in daterange(start_date, end_date):
        date_obj = datetime.combine(single_date, datetime.min.time())
        value = c.get_rate((select_arverage_box.get()).upper(), (convert_arverage_box.get()).upper(), date_obj)
        total = single_date.strftime('%Y-%m-%d:'), value
        numbers += value
        print(total)
    arverage_result_label.configure(text=numbers/((int(end_day_box.get())+1)-int(start_day_box.get())))

def predict_leftclickbutton(event):
    c = CurrencyRates()
    start_date = date(2021, 3, 1)
    end_date = date(2021, int(convert_month_box.get()), int(convert_day_box.get()))
    numbers = 0
    value = 0

    for single_date in daterange(start_date, end_date):
        date_obj = datetime.combine(single_date, datetime.min.time())
        value = c.get_rate((select_predict_box.get()).upper(), (convert_predict_box.get()).upper(), date_obj)
        numbers += value
    avr = numbers / (int(convert_day_box.get()) - 1)
    per = abs(((avr*100 )/ value)-100)
    predict_result_label.configure(text=per)
root = Tk()
title_currency = root.title('Currency Program')
welcome_label = Label(root, text="Welcome to Currency Program.",font=30)
welcome_label.grid(row=0,column=0)
#arverage_zone
arverage_menu = Label(root, text="1.Currency arverage",font=1,bg='orange')
arverage_menu.grid(row=1,column=0)

select_arverage_label = Label(root, text="Currency do u want : ")
select_arverage_label.grid(row=2,column=0)

convert_arverage_label = Label(root, text="Convert with : ")
convert_arverage_label.grid(row=3,column=0)

select_arverage_box = Entry(root,width=5)
select_arverage_box.grid(row=2,column=1)

convert_arverage_box = Entry(root,width=5)
convert_arverage_box.grid(row=3,column=1)

start_date_label = Label(root, text="Year/Month/Day(start) : ")
start_date_label.grid(row=2,column=3)

start_year_box = Entry(root,width=5)
start_year_box.grid(row=2,column=4)

start_month_box = Entry(root,width=4)
start_month_box.grid(row=2,column=5)

start_day_box = Entry(root,width=4)
start_day_box.grid(row=2,column=6)

end_date_label = Label(root, text="Year/Month/Day(end) : ")
end_date_label.grid(row=3,column=3)

end_year_box = Entry(root,width=5)
end_year_box.grid(row=3,column=4)

end_month_box = Entry(root,width=4)
end_month_box.grid(row=3,column=5)

end_day_box = Entry(root,width=4)
end_day_box.grid(row=3,column=6)

arverage_button = Button(root,text ="calculate",bg='orange')
arverage_button.grid(row=4,column=0)
arverage_button.bind('<Button-1>',arverage_leftclickbutton)

arverage_result_label = Label(root, text="result")
arverage_result_label.grid(row=4,column=1)

emptyspace = Label(root)
emptyspace.grid(row=5,column=1)

#predict_zone

arverage_menu = Label(root, text="2.Predict Currency",font=1,bg='orange')
arverage_menu.grid(row=6,column=0)

warning_currency_label = Label(root, text="This process start at 1 mar 2021 cant predict year past")
warning_currency_label.grid(row=7,column=0)

warning2_currency_label = Label(root, text="Available from 1 March 2021  onwards")
warning2_currency_label.grid(row=8,column=0)

select_predict_label = Label(root, text="Currency do u want : ")
select_predict_label.grid(row=9,column=0)

convert_predict_label = Label(root, text="Convert with : ")
convert_predict_label.grid(row=10,column=0)

select_predict_box = Entry(root,width=5)
select_predict_box.grid(row=9,column=1)

convert_predict_box = Entry(root,width=5)
convert_predict_box.grid(row=10,column=1)

convert_date_label = Label(root, text="Month/Day : ")
convert_date_label.grid(row=9,column=3)

convert_month_box = Entry(root,width=4)
convert_month_box.grid(row=9,column=5)

convert_day_box = Entry(root,width=4)
convert_day_box.grid(row=9,column=6)

predict_button = Button(root,text ="calculate",bg='orange')
predict_button.grid(row=11,column=0)
predict_button.bind('<Button-1>',predict_leftclickbutton)

predict_result_label = Label(root, text="result(+-percentage)")
predict_result_label.grid(row=11,column=1)

emptyspace2 = Label(root)
emptyspace2.grid(row=12,column=1)

root.resizable(width=False, height=False)
root.mainloop()