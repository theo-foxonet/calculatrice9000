from tkinter import *

root = Tk()
root.title("Calculatrice9000")

e = Entry(root, width=55, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_equal():
    number = e.get()
    e.delete(0, END)
    e.insert(0, eval(number))

def button_sqrt():
    current = e.get()
    e.delete(0, END)
    e.insert(0, pow(float(current), 0.5))

def button_percent():
    current = e.get()
    e.delete(0, END)
    e.insert(0, float(current) / 100)





button_1 = Button(root, text="1", padx=40, pady=20, command=lambda:button_click('1'))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda:button_click('2'))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda:button_click('3'))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda:button_click('4'))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda:button_click('5'))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda:button_click('6'))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda:button_click('7'))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda:button_click('8'))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda:button_click('9'))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda:button_click('0'))
button_c = Button(root, text="C", padx=40, pady=20, command=lambda:button_clear())
button_plus = Button(root, text="+", padx=40, pady=20, command=lambda:button_click('+'))
button_moins = Button(root, text="-", padx=40, pady=20, command=lambda:button_click('-'))
button_division = Button(root, text="/", padx=40, pady=20, command=lambda:button_click('/'))
button_multiplication = Button(root, text="*", padx=40, pady= 20, command=lambda:button_click('*'))
button_sqrt = Button(root, text="√x", padx=40, pady=20, command=button_sqrt)
button_percent = Button(root, text="%", padx=40, pady=20, command=button_percent)
button_e = Button(root, text="=", padx=40, pady=20, command=lambda:button_equal())

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_c.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_plus.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_moins.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_division.grid(row=4, column=1)
button_multiplication.grid(row=4, column=2)
button_sqrt.grid(row=5, column=0)
button_percent.grid(row=5, column=1)
button_e.grid(row=4, column=3)


root.mainloop()