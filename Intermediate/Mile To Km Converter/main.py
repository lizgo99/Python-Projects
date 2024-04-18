from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def calculate(): ## check if int
    miles = input.get()
    num_of_km_label.config(text= str(float(miles) * 1.609344))
       

input = Entry(width=7)
input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

eq_label = Label(text="is equal to")
eq_label.grid(row=1, column=0)

num_of_km_label = Label(text="0")
num_of_km_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

button = Button(text= "Calculate", command= calculate)
button.grid(row=2, column=1)





window.mainloop()