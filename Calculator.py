from tkinter import *
import math
base = Tk()
base.title("Calculator")
"""
sets up the "entry box"... where users sees the numbers
"""
user_entry = Entry(base, width=45)
user_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def clicked(number):
    current = user_entry.get()
    user_entry.delete(0, END)
    user_entry.insert(10, str(current)+ str(number))
"""
creates the clear button logic
"""
def clear() -> None:
    user_entry.delete(0, END)

""" 
sets up logic for the equals button
"""
def equal():
    num_two = user_entry.get()
    user_entry.delete(0, END)

    if math == 'addition':
        user_entry.insert(0, f_num + int(num_two))

    if math == 'subtraction':
        user_entry.insert(0, f_num - int(num_two))

    if math == 'multiplication':
        user_entry.insert(0, f_num * int(num_two))

    if math == 'division':
        user_entry.insert(0, f_num / int(num_two))

"""
sets up logic for cosine
"""
def cosine():
	first_number = user_entry.get()
	global f_num
	f_num = float(first_number)
	cos_val=round((math.cos(math.radians(f_num))),2)
	user_entry.insert(0,cos_val)
"""
sets up logic for ine
"""
def sine():
	first_number = user_entry.get()
	global f_num
	f_num = float(first_number)
	sin_val=round((math.sin(math.radians(f_num))),2)
	user_entry.insert(0,sin_val)
"""
sets up logic for tangent
"""
def tangent():
	first_number = user_entry.get()
	global f_num
	f_num = float(first_number)
	tan_val=round((math.tan(math.radians(f_num))),2)
	user_entry.insert(0,tan_val)

"""
sets up logic for addition button
"""
def add():
    num_one = user_entry.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(num_one)
    user_entry.delete(0, END)

"""
sets up logic for subtraction
"""

def subtraction():
    num_one = user_entry.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(num_one)
    user_entry.delete(0, END)
"""
sets up logic for multiplication
"""
def multiply():
    num_one = user_entry.get()
    global f_num
    global math
    math = ('multiplication')
    f_num = int(num_one)
    user_entry.delete(0, END)
"""
sets up logic for division
"""
def divide():
    num_one = user_entry.get()
    global f_num
    global math
    math = 'division'
    f_num = int(num_one)
    user_entry.delete(0, END)
"""
sets up the buttons 
"""
btn_one = Button(base, text="1", padx=45, pady=20, command=lambda: clicked(1))
btn_two = Button(base, text="2", padx=45, pady=20, command=lambda: clicked(2))
btn_three = Button(base, text="3", padx=45, pady=20, command=lambda: clicked(3))
btn_four = Button(base, text="4", padx=45, pady=20, command=lambda: clicked(4))
btn_five = Button(base, text="5", padx=45, pady=20, command=lambda: clicked(5))
btn_six = Button(base, text="6", padx=45, pady=20, command=lambda: clicked(6))
btn_seven = Button(base, text="7", padx=45, pady=20, command=lambda: clicked(7))
btn_eight = Button(base, text="8", padx=45, pady=20, command=lambda: clicked(8))
btn_nine = Button(base, text="9", padx=45, pady=20, command=lambda: clicked(9))
btn_zero = Button(base, text="0", padx=45, pady=20, command=lambda: clicked(0))
btn_cos= Button(base,text='cos',padx=45,pady=20, command=cosine)
btn_sin= Button(base,text='sin',padx=45,pady=20, command=sine)
btn_tan= Button(base,text='tan',padx=45,pady=20, command=tangent)
btn_add = Button(base, text="+", padx=45, pady=20, command=add)
btn_equal = Button(base, text="=", padx=45, pady=20, command=equal)
btn_clear = Button(base, text="C", padx=45, pady=20, command=clear)

btn_subtract = Button(base, text="-", padx=45, pady=20, command=subtraction)
btn_multiply = Button(base, text="x", padx=45, pady=20, command=multiply)
btn_divide = Button(base, text="/", padx=45, pady=20, command=divide)

"""
Put the buttons on the screen (calculator)
"""

btn_one.grid(row=1, column=0)
btn_two.grid(row=1, column=1)
btn_three.grid(row=1, column=2)

btn_four.grid(row=2, column=0)
btn_five.grid(row=2, column=1)
btn_six.grid(row=2, column=2)

btn_seven.grid(row=3, column=0)
btn_eight.grid(row=3, column=1)
btn_nine.grid(row=3, column=2)
btn_zero.grid(row=4, column=1)

btn_cos.grid(row=5,column=0)
btn_sin.grid(row=6,column=0)
btn_tan.grid(row=7,column=0)


btn_clear.grid(row=7, column=1)
btn_equal.grid(row=7, column=2)

btn_add.grid(row=5, column=1)
btn_subtract.grid(row=5, column=2)
btn_multiply.grid(row=6, column=1)
btn_divide.grid(row=6, column=2)
base.mainloop()
