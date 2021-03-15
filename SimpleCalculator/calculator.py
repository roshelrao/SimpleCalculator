import random 
from tkinter import * 
from tkinter import messagebox 

window = Tk()

window.geometry("200x200")

Label1 = Label(window, text="Number one")
Label1.pack()

num1 = Entry(window,bg="white")
num1.pack()

Label2 = Label(window, text="Number two")
Label2.pack()

num2 = Entry(window,bg="white")
num2.pack()

Label3 = Label(window, text="Answer")
Label3.pack()

answer = Entry(window, bg="white")
answer.pack()

number1=0
number2=0
result=0

def add():
    number1=int(num1.get())
    number2=int(num2.get())

    result=number1+number2
    answer.insert(0,result)

def sub():
    number1=int(num1.get())
    number2=int(num2.get())

    result=number1-number2
    answer.insert(0,result)

def mul():
    number1=int(num1.get())
    number2=int(num2.get())

    result=number1*number2
    answer.insert(0,result)

def div():
    number1=int(num1.get())
    number2=int(num2.get())

    result=number1/number2
    answer.insert(0,result)

button_add = Button(window,text="+",command=add,bg="#AEC6CF", width=4,height=2,relief="flat")
button_sub = Button(window,text="-",command=sub,bg="#AEC6CF", width=4,height=2,relief="flat")
button_mul = Button(window,text="*",command=mul,bg="#AEC6CF", width=4,height=2,relief="flat")
button_div = Button(window,text="/",command=div,bg="#AEC6CF", width=4,height=2,relief="flat")

button_add.pack(side=LEFT,padx=(20,2))
button_sub.pack(side=LEFT,padx=2)
button_mul.pack(side=LEFT,padx=2)
button_div.pack(side=LEFT,padx=2)

window.mainloop()



