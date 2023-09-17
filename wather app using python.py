# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 18:36:37 2023

@author: USER
"""

from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=594cb4ff24786f8dc938243e8df48c75").json()
    w_lable1.config(text=data["weather"][0]["main"])
    wb_lable1.config(text=data["weather"][0]["description"])
    temp_lable1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_lable1.config(text=data["main"]["pressure"])
    
    
win = Tk()

win.title("Himanshu parmar")

win.config(bg = "aqua")

win.geometry("500x580")

name_lable = Label(win,text="Weather App",font=("Time New Roman",
                                                25,"bold"))

name_lable.place(x=25,y=50,height=50,width=450)

city_name = StringVar() 

list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win,text="Weather App",values=list_name,
                    font=("Time New Roman",
                    20,"bold"),textvariable=city_name)

com.place(x=25,y=120,height=55,width=450)


w_lable = Label(win,text="Weather Climate",font=("Time New Roman",
                                                15))

w_lable.place(x=25,y=275,height=60,width=200)

w_lable1 = Label(win,text="",font=("Time New Roman",
                                                15))

w_lable1.place(x=235,y=275,height=60,width=200)



wb_lable = Label(win,text="Weather Description",font=("Time New Roman",
                                                15))

wb_lable.place(x=25,y=345,height=60,width=200)  

wb_lable1 = Label(win,text="",font=("Time New Roman",
                                                15))

wb_lable1.place(x=235,y=345,height=60,width=200)
  


temp_lable = Label(win,text="Temperature",font=("Time New Roman",
                                                15))

temp_lable.place(x=25,y=415,height=60,width=200)

temp_lable1 = Label(win,text="",font=("Time New Roman",
                                                15))

temp_lable1.place(x=235,y=415,height=60,width=200)   


per_lable = Label(win,text="Pressure",font=("Time New Roman",
                                                15))

per_lable.place(x=25,y=485,height=60,width=200)

per_lable1 = Label(win,text="",font=("Time New Roman",
                                                15))

per_lable1.place(x=235,y=485,height=60,width=200) 

done_button = Button(win,text="Done",
                    font=("Time New Roman",
                    20,"bold"),command=data_get) 


done_button.place(y=195,height=50,width=100,x=200)


win.mainloop() 

