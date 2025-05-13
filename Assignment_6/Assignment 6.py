from tkinter import *

window = Tk()
window.geometry("400x500")


e = Entry(window,width = 60,borderwidth= 5)
e.place(x=0, y=0)

#Buttons

def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0,str(result) + str(num))

b = Button(window,text = '1',width = 10,command= lambda : click(1))
b.place(x = 20, y = 40)

b = Button(window,text = '2',width = 10,command= lambda : click(2))
b.place(x = 110, y = 40)

b = Button(window,text = '3',width = 10,command= lambda : click(3))
b.place(x = 200, y = 40)

b = Button(window,text = '4',width = 10,command= lambda : click(4))
b.place(x = 20, y = 80)

b = Button(window,text = '5',width = 10,command= lambda : click(5))
b.place(x = 110, y = 80)

b = Button(window,text = '6',width = 10,command= lambda : click(6))
b.place(x = 200, y = 80)

b = Button(window,text = '7',width = 10,command= lambda : click(7))
b.place(x = 20, y = 120)

b = Button(window,text = '8',width = 10,command= lambda : click(8))
b.place(x = 110, y = 120)

b = Button(window,text = '9',width = 10,command= lambda : click(9))
b.place(x = 200, y = 120)

b = Button(window,text = '0',width = 10,command= lambda : click(0))
b.place(x = 20, y = 160)

def add():
    n1 = e.get()
    global math
    math = "Addition"
    global i
    i = int(n1)
    e.delete(0,END)
b = Button(window,text = '+',width = 10,command= add)
b.place(x = 110, y = 160)

def sub():
    n1 = e.get()
    global math
    math = "Subtraction"
    global i
    i = int(n1)
    e.delete(0,END)
b = Button(window,text = '-',width = 10,command = sub)
b.place(x = 200, y = 160)

def mul():
    n1 = e.get()
    global math
    math = "Multiplication"
    global i
    i = int(n1)
    e.delete(0,END)
b = Button(window,text = '*',width = 10,command= mul)
b.place(x = 20, y = 200)

def div():
    n1 = e.get()
    global math
    math = "Division"
    global i
    i = int(n1)
    e.delete(0,END)
b = Button(window,text = '/',width = 10,command= div)
b.place(x = 110, y = 200)


def equal():
    n2 = e.get()
    e.delete(0,END)
    if math == "Addition":
        e.insert(0, i + int(n2))
    elif math == "Subtraction":
        e.insert(0, i - int(n2))
    elif math == "Multiplication":
        e.insert(0, i * int(n2))
    elif math == "Division":
        e.insert(0, "Error" if int(n2) == 0 else i / int(n2))

b = Button(window,text = '=',width = 10,command=equal)
b.place(x = 200, y = 200)


def clear():
    e.delete(0,END)
b = Button(window,text = 'clear',width = 10,command= clear)
b.place(x = 20, y = 240)


window.mainloop()








