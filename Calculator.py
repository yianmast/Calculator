### A calculator GUI with tkinter library

from tkinter import *

###=================================================================================================================================
""" All the function for the calculator: btn identifinder, clear btn and equal btn"""

### identifies the number clicked exclude thr btns clear(C) and equal(=) and put them in the txtDisplay
def btnClick(number):         
    global operator
    operator = operator + str(number)
    numb.set(operator)
    
###function for the btn C. It cleares the screen           
def clear():
    global operator
    operator = ""
    numb.set("")
    
###function for the btn =. It makes the calculations
def equal():
    global operator
    sum = str(eval(operator))
    numb.set(sum)
    operator = ""   
###================================================================================================================================
"""Using tkinter I created the GUI"""
###
#   1 2 3 +
#   4 5 6 -
#   7 8 9 *
#   C 0 = /
###
root = Tk()
frame = Frame(root)
frame.pack()
root.title('Calculator')
operator = ""
numb = StringVar()
txtDisplay = Entry(frame, textvariable = numb, bd = 50, insertwidth = 8, font = 4, bg = "violet")
txtDisplay.pack(side = TOP)

###=================================================================================================================================
#   1 2 3 +
###
frame = Frame(root)
frame.pack(side = TOP)

button1 = Button(frame, padx=16, pady=16, bd=10, text = '1', fg = "blue", font = 40, bg = "orange red", command=lambda:btnClick(1))
button1.pack(side = LEFT)

button2 = Button(frame, padx=16, pady=16, bd=10, text = '2', fg = "blue", font = 40, bg = "orange red", command=lambda:btnClick(2))
button2.pack(side = LEFT)

button3 = Button(frame, padx=16, pady=16, bd=10, text = '3', fg = "blue", font = 40, bg = "orange red", command=lambda:btnClick(3))
button3.pack(side = LEFT)

buttonPlus = Button(frame, padx=16, pady=16, bd=10, text = '+', fg = "blue", font = 40, bg = "orange red", command=lambda:btnClick('+'))
buttonPlus.pack(side = LEFT)
###=================================================================================================================================
#   4 5 6 -
###
frame1 = Frame(root)
frame1.pack(side = TOP)

button4 = Button(frame1, padx=16, pady=16, bd=10, text = '4', fg = "blue", font = 40, bg = "orange red", command=lambda:btnClick(4))
button4.pack(side = LEFT)

button5 = Button(frame1, padx=16, pady=16, bd=10, text = '5', fg = "blue", font = 40, bg = "orange red", command=lambda:btnClick(5))
button5.pack(side = LEFT)

button6 = Button(frame1, padx=16, pady=16, bd=10, text = '6', fg = "blue", font = 40, bg = "orange red", command=lambda:btnClick(6))
button6.pack(side = LEFT)

buttonMinus = Button(frame1, padx=16, pady=16, bd=10, text = '-', fg = "blue", font = 40, bg = "orange red", command=lambda:btnClick("-"))
buttonMinus.pack(side = LEFT)

###=================================================================================================================================
#   7 8 9 *
###
frame2 = Frame(root)
frame2.pack(side = TOP)

button7 = Button(frame2, padx=16, pady=16, bd=10, text = '7', fg = "blue", font = 40, bg = "orange red", command=lambda:btnClick(7))
button7.pack(side = LEFT)

button8 = Button(frame2, padx=16, pady=16, bd=10, text = '8', fg = "blue", font = 40, bg = "orange red", command=lambda:btnClick(8))
button8.pack(side = LEFT)

button9 = Button(frame2, padx=16, pady=16, bd=10, text = '9', fg = "blue", font = 40, bg = "orange red", command=lambda:btnClick(9))
button9.pack(side = LEFT)

buttonMult = Button(frame2, padx=16, pady=16, bd=10, text = '*', fg = "blue", font = 40, bg = "orange red", command=lambda:btnClick('*'))
buttonMult.pack(side = LEFT)
###=================================================================================================================================
#   C 0 = /
###
frame3 = Frame(root)
frame3.pack(side = TOP)

buttonC = Button(frame3, padx=16, pady=16, bd=10, text = 'C', fg = "blue", font = 40, bg = "orange red",command = clear)
buttonC.pack(side = LEFT)

button0 = Button(frame3, padx=16, pady=16, bd=10, text = '0', fg = "blue", font = 40, bg = "orange red", command=lambda:btnClick(0))
button0.pack(side = LEFT)

buttonEq = Button(frame3, padx=16, pady=16, bd=10, text = '=', fg = "blue", font = 40, bg = "orange red", command=equal)
buttonEq.pack(side = LEFT)

buttonDiv = Button(frame3, padx=16, pady=16, bd=10, text = '/', fg = "blue", font = 40, bg = "orange red", command=lambda:btnClick('/'))
buttonDiv.pack(side = LEFT)


root.mainloop()
