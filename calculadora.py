from tkinter import *
import parser

def get_numbers(num) :
    global indice
    display.insert(indice, num)
    indice += 1

def get_operation(operator) :
    global indice
    display.insert(indice, operator)
    indice += len(operator)

def clear_display() :
    display.delete(0, END)

def undo_display() :
    state = display.get()
    if len(state) :
        display.delete(0, END)
        new_state = state[: -1]
        display.insert(0, new_state)
    else :
        display.delete(0, END)
        display.insert(0, "Error")

def calculate() :
    state = display.get()
    try :
        math_expresion = parser.expr(state).compile()
        result = eval(math_expresion)
        display.delete(0, END)
        display.insert(0, result)
    except :
        display.delete(0, END)
        display.insert(0, "Error")

indice = 0
root = Tk()
root.title("Calculadora")

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

#Numeric Buttons
Button(root, text="1", command=lambda:get_numbers(1)).grid(row=2, column=0, sticky=W+E)
Button(root, text="2", command=lambda:get_numbers(2)).grid(row=2, column=1, sticky=W+E)
Button(root, text="3", command=lambda:get_numbers(3)).grid(row=2, column=2, sticky=W+E)

Button(root, text="4", command=lambda:get_numbers(4)).grid(row=3, column=0, sticky=W+E)
Button(root, text="5", command=lambda:get_numbers(5)).grid(row=3, column=1, sticky=W+E)
Button(root, text="6", command=lambda:get_numbers(6)).grid(row=3, column=2, sticky=W+E)

Button(root, text="7", command=lambda:get_numbers(7)).grid(row=4, column=0, sticky=W+E)
Button(root, text="8", command=lambda:get_numbers(8)).grid(row=4, column=1, sticky=W+E)
Button(root, text="9", command=lambda:get_numbers(9)).grid(row=4, column=2, sticky=W+E)

#Operaciones Buttons
Button(root, text="AC", command=lambda:clear_display()).grid(row=5, column=0, sticky=W+E)
Button(root, text="0", command=lambda:get_numbers(0)).grid(row=5, column=1, sticky=W+E)
Button(root, text="%", command=lambda:get_operation("%")).grid(row=5, column=2, sticky=W+E)
Button(root, text="+", command=lambda:get_operation("+")).grid(row=2, column=3, sticky=W+E)
Button(root, text="-", command=lambda:get_operation("-")).grid(row=3, column=3, sticky=W+E)
Button(root, text="*", command=lambda:get_operation("*")).grid(row=4, column=3, sticky=W+E)
Button(root, text="/", command=lambda:get_operation("/")).grid(row=5, column=3, sticky=W+E)
Button(root, text="DEL", command=lambda:undo_display()).grid(row=2, column=4, sticky=W+E, columnspan = 2)
Button(root, text="exp", command=lambda:get_operation("**")).grid(row=3, column=4, sticky=W+E)
Button(root, text="^2", command=lambda:get_operation("**2")).grid(row=3, column=5, sticky=W+E)
Button(root, text="(", command=lambda:get_operation("(")).grid(row=4, column=4, sticky=W+E)
Button(root, text=")", command=lambda:get_operation(")")).grid(row=4, column=5, sticky=W+E)
Button(root, text="=", command=lambda:calculate()).grid(row=5, column=4, sticky=W+E, columnspan = 2)

root.mainloop()
