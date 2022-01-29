from tkinter import *

def leftclickbutton(event):
   LableResalt.configure(text =int(textBoxWeight.get())//((float(textBoxHeight.get())/100)**2))
   Resalt = int(textBoxWeight.get())//((float(textBoxHeight.get())/100)**2)
   if int(Resalt) > 30:
      Labletotal.configure(text = "อ้วนมาก",bg='orange')
   elif int(Resalt) >= 25:
      Labletotal.configure(text = "อ้วน",bg='orange')
   elif int(Resalt) >= 23:
      Labletotal.configure(text="น้ำหนักเกิน",bg='orange')
   elif int(Resalt) >= 18.6:
      Labletotal.configure(text="น้ำหนักปกติ เหมาะสม",bg='orange')
   else:
      Labletotal.configure(text="ผอมเกินไป",bg='orange')

MainWindow = Tk()
LableHeight = Label(MainWindow,text = "ส่วนสูง (cm)")
LableHeight.grid(row=0,column=0)

textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)

LableWeight = Label(MainWindow,text = "น้ำหนัก (Kg)")
LableWeight.grid(row=1,column=0)

textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

CalculateButton = Button(MainWindow,text ="คำนวณ",bg='orange')
CalculateButton.grid(row=2,column=0)
CalculateButton.bind('<Button-1>', leftclickbutton)

LableResalt = Label(MainWindow,text = "ผลลัพธ์")
LableResalt.grid(row=2,column=1)

Labletotal = Label(MainWindow)
Labletotal.grid(row=3,column=1)

MainWindow.mainloop()