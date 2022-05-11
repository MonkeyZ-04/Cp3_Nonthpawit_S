from tkinter import *
import requests
import time


def getWeather(event):
    city = entry0.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
    #Start Editing
    label1.config(text=str(temp)+"°C")
    label2.config(text=condition)
    label3.config(text=str(min_temp) + "°C")
    label4.config(text=str(max_temp) + "°C")
    label5.config(text=" : "+str(pressure))
    label6.config(text=" : "+str(humidity))
    label7.config(text=" : "+str(wind))
    label8.config(text=sunrise)
    label9.config(text=sunset)

window = Tk()
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

window.geometry("692x415")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 415,
    width = 692,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file =f"background.png")
background = canvas.create_image(
    346.0, 207.0,
    image=background_img)

img0 = PhotoImage(file =f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = getWeather,
    relief = "flat")

b0.place(
    x = 395, y = 68,
    width = 56,
    height = 56)

b0.bind('<Button>',getWeather)

entry0_img = PhotoImage(file =f"img_textBox0.png")
entry0_bg = canvas.create_image(
    258.0, 96.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0,
    font=("poppins", 30, "bold"))

entry0.place(
    x = 155.0, y = 68,
    width = 206.0,
    height = 54)
# Start Editing
label1 = Label(window,font=("Gill Sans", 40, "bold"),fg="#00A4EF",bg="white")
label1.place(
    x = 127, y = 139,
    width = 149,
    height = 44)

label2 = Label(window,font=("Gill Sans", 35, "bold"),fg="#00A4EF",bg="white",justify='left')
label2.place(
    x = 461, y = 88,
    width = 173,
    height = 102)

label3 = Label(window,font=("Gill Sans", 18, "bold"),fg="#F3F3F3",bg="#F25022")
label3 .place(
    x = 585, y = 275,
    width = 52,
    height = 18)

label4 = Label(window,font=("Gill Sans", 18, "bold"),fg="#F3F3F3",bg="#F25022")
label4 .place(
    x = 582, y = 327,
    width = 52,
    height = 18)

label5 = Label(window,font=("Gill Sans", 20, "bold"),fg="#F3F3F3",bg="#00A4EF")
label5 .place(
    x = 300, y = 267,
    width = 90,
    height = 25)

label6 = Label(window,font=("Gill Sans", 20, "bold"),fg="#F3F3F3",bg="#00A4EF")
label6 .place(
    x = 435, y = 267,
    width = 71,
    height = 25)

label7 = Label(window,font=("Gill Sans", 20, "bold"),fg="#F3F3F3",bg="#00A4EF")
label7 .place(
    x = 298, y = 320,
    width = 90,
    height = 25)

label8 = Label(window,font=("Gill Sans", 16, "bold"),fg="#F3F3F3",bg="#FFB900")
label8 .place(
    x = 105, y = 272,
    width = 85,
    height = 17)

label9 = Label(window,font=("Gill Sans", 16, "bold"),fg="#F3F3F3",bg="#231815")
label9 .place(
    x = 105, y = 327,
    width = 85,
    height = 17)

window.resizable(False, False)
window.mainloop()
