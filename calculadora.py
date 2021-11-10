from tkinter import *

root = TK()
root.title("Calculadora")

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

Button(root, text="1").grid()
root.mainloop()
