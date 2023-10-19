import requests
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk



def gettemprates():
    try:
        amount = float(var__num.get())
        from_temp = var_fromtemp_num.get().lower()
        to_temp = var_totemp_num.get().lower()
        if from_temp=='celsius':
            if to_temp=='kelvin':
                amount = amount + 273.15
            elif to_temp=='farenheit':
                amount = amount*(9/5) + 32
            elif to_temp == 'celsius':
                amount = amount
        elif from_temp=='kelvin':
            if to_temp=='kelvin':
                amount = amount
            elif to_temp=='farenheit':
                amount = (amount-273.15) * (9/5) + 32
            elif to_temp == 'celsius':
                amount = amount - 273.15
        elif from_temp =='farenheit':
            if to_temp=='kelvin':
                amount = (amount-32) * (5/9) + 273.15
            elif to_temp=='farenheit':
                amount = amount
            elif to_temp == 'celsius':
                amount = (amount-32) * (5/9)
     
        var_result.set(f"{amount:.3f}  {var_totemp_num.get().capitalize()}")
    except:
        var_result.set("Error")

def clearResult():
    var__num.set("")
    var_fromtemp_num.set("")
    var_totemp_num.set("")
    var_result.set("")
root = Tk()
root.geometry('800x600')

root.title('temp Converter')
root.config(background='#040505')
# bg_image = ImageTk.PhotoImage("c")
# original_image = Image.open(r"converter.jpg")
# resized_image = original_image.resize((100, 100))
# icon_title = ImageTk.PhotoImage(resized_image)
title = Label(root,text="Temperature Converter",justify=CENTER,font=('times',28,"bold"),foreground='white',background='#040505',borderwidth=2,relief=SUNKEN,padx=20)
title.place(x=220,y=10,height=102,width=400)
line=Label(root,background='#0C1CE1').place(x=0,y=117,relwidth=1,height=2)
# title2 =Label(root, text="Created By Awais",justify=CENTER,font=("roboto",24,'bold'),bg='#1EECE9',fg='White',padx=5).place(x=0,y=105,relwidth=1,height=30)


var__num = StringVar()
var_totemp_num = StringVar()
var_fromtemp_num = StringVar()
var_result= StringVar()



lbl_totemp_num = Label(root, text="Amount", font=("goudy old style", 15,'bold'),background='black',fg='white').place(x=280, y=170)
lbl_totemp_num = Label(root, text="From temp", font=("goudy old style", 15,'bold'),background='black',fg='white').place(x=280, y=230)
lbl_fromtemp_num = Label(root, text="To temp", font=("goudy old style", 15,'bold'),background='black',fg='white').place(x=280, y=290)
# cmb_gender = ttk.Combobox(self.root, textvariable=self.var_searchby, values=("Select", "Male", "Female", "Others"),
#                                   state="readonly", justify=CENTER, font=("goudy old style", 15))
#         cmb_gender.place(x=500, y=150, width=180)
#         cmb_gender.current(0)

txt_first_num = Entry(root,textvariable=var__num,font=("goudy old style",16),bg="white").place(x=265,y=200)
txt_firstchoice_num = ttk.Combobox(root, textvariable=var_fromtemp_num, values=('select',"Celsius","Kelvin","Farenheit",),state='readonly',justify=CENTER,font=("goudy old style",15))
txt_firstchoice_num.place(x=265,y=260)
txt_firstchoice_num.current(0)
txt_secondchoice_num = ttk.Combobox(root, textvariable=var_totemp_num, values=('select',"Celsius","Kelvin","Farenheit",),state='readonly',justify=CENTER,font=("goudy old style",15))
txt_secondchoice_num.place(x=265,y=320)
txt_secondchoice_num.current(0)


btn_add = Button(root, text="Get",command=gettemprates, font=("goudy old style", 12),bg="#4caf50", fg="white", cursor="hand2").place(x=265,y=370, width=95, height=30)
btn_add = Button(root, text="Clear",command=clearResult, font=("goudy old style", 12),bg="red", fg="white", cursor="hand2").place(x=375,y=370, width=95, height=30)

txt_first_num = Entry(root,textvariable=var_result,font=("Roboto",15,"bold"),fg="#DAD719",bg="#3B3333",borderwidth=2,relief=SUNKEN,width=35).place(x=210,y=420)


texti = Label(root, text="Powered By Maham",fg="#0C1CE1",font=("times",12),bg='black').place(x=0,y=575)
texti = Label(root, text="Version 1.1",fg="#0C1CE1",font=("times",12),bg='black').place(x=715,y=575)


root.mainloop()