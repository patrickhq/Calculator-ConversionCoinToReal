from tkinter import *
from tkinter import ttk
from decimal import Decimal



# Colors
col1 = "#2e2d2d" #black/ preto
col2 = "#feffff" #white/ branco
col3 = "#38576b" #blue/ azul
col4 = "#ECEFF1" #gray/ Cinza
col5 = "#427d5c" #Green/ Verde
col6 = "#000000" #black100%

#window config
window = Tk()
window.title("Calculadora")
window.geometry("450x550") #Area da janela
window.config(bg=col1)

#display config
frame_display = Frame(window, width=450, height=80, bg=col3)
frame_display.grid(row = 0, column = 0)

#body / corpo
frame_body = Frame(window, width=448, height=470, bg=col1)
frame_body.grid(row = 1, column = 0)


all_values = ''

#Functions

def values(event):
    global all_values
    all_values = all_values + str(event)

    #send to display
    text_value.set(all_values)

def calculate():
    global all_values

    result = Decimal(eval(all_values))

    text_value.set(str(result))

def cleanDisplay():
    global all_values
    all_values=""
    text_value.set("")

def backspace():
    global all_values
    all_values=all_values[:-1]
    text_value.set(all_values)

def dolar():
    global all_values

    dolar = 5.22*eval(all_values)


    text_value.set(str(dolar))

def euro():
    global all_values

    euro = 5.57*eval(all_values)

    text_value.set(str(euro))

def iene():
    global all_values

    iene = 0.0385*eval(all_values)

    text_value.set(str(iene))

def libraEsterlina():
    global all_values

    libraE = 6.21*eval(all_values)

    text_value.set(str(libraE))

#Label
text_value = StringVar()

app_Label = Label(frame_display, textvariable=text_value, width=16, height=2, padx=130, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 25'), bg=col3, fg=col2)
app_Label.place(x=0,y=0)

#Buttons / Botões
b1 = Button(frame_body,command=cleanDisplay, text = "C", width= 29, height=4, bg=col4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=7, y=4)

b2 = Button(frame_body,command=lambda:values('%'),text = "%", width= 13, height=4, bg=col5, fg=col2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=228, y=4)

b3 = Button(frame_body,command=lambda:values('*'), text = "X", width= 13, height=4, bg=col5, fg=col2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=338, y=4)

b4 = Button(frame_body,command=lambda:values('7'), text = "7", width= 13, height=4, bg=col4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=7, y=80)

b5 = Button(frame_body,command=lambda:values('8'), text = "8", width= 13, height=4, bg=col4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=118, y=80)

b6 = Button(frame_body,command=lambda:values('9'), text = "9", width= 13, height=4, bg=col4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=228, y=80)

b6 = Button(frame_body,command=lambda:values('/'), text = "/", width= 13, height=4, bg=col5, fg=col2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=338, y=80)

b7 = Button(frame_body,command=lambda:values('4'), text = "4", width= 13, height=4, bg=col4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=7, y=158)

b8 = Button(frame_body,command=lambda:values('5'), text = "5", width= 13, height=4, bg=col4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=118, y=158)

b9 = Button(frame_body,command=lambda:values('6'), text = "6", width= 13, height=4, bg=col4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=228, y=158)

b10 = Button(frame_body,command=lambda:values('+'), text = "+", width= 13, height=4, bg=col5, fg=col2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=338, y=158)

b11 = Button(frame_body,command=lambda:values('1'), text = "1", width= 13, height=4, bg=col4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=7, y=236)

b12 = Button(frame_body,command=lambda:values('2'), text = "2", width= 13, height=4, bg=col4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=118, y=236)

b13 = Button(frame_body,command=lambda:values('3'), text = "3", width= 13, height=4, bg=col4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=228, y=236)

b14 = Button(frame_body,command=lambda:values('-'), text = "-", width= 13, height=4, bg=col5, fg=col2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=338, y=236)

b8 = Button(frame_body,command=libraEsterlina, text = "£", width= 13, height=4, bg=col4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=7, y=314)

b9 = Button(frame_body,command=lambda:values('0'), text = "0", width= 13, height=4, bg=col4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=118, y=314)

b10 = Button(frame_body,command=lambda:values('.'), text = ".", width= 13, height=4, bg=col4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=228, y=314)

b11 = Button(frame_body,command=backspace, text = "⌫", width= 13, height=4, bg=col5, fg=col2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=338, y=314)

b8 = Button(frame_body,command=dolar, text = "US", width= 13, height=4, bg=col4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=7, y=392)

b9 = Button(frame_body,command=euro, text = "€", width= 13, height=4, bg=col4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=118, y=392)

b10 = Button(frame_body,command=iene, text = "¥", width= 13, height=4, bg=col4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=228, y=392)

b11 = Button(frame_body,command=calculate, text = "=", width= 13, height=4, bg=col5, fg=col2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=338, y=392)


window.mainloop()
