import tkinter

#Základní nastavení okna
window = tkinter.Tk()
window.geometry("300x200")
window.title("Basic Calculator")

#První číslo - Vytvoření layoutu a zarovnání do mřížky(gridu).
label_number_1 = tkinter.Label(window, text="Enter first number: ")
label_number_1.grid(row="0", column="0")
value_number_1 = tkinter.Entry(window)
value_number_1.grid(row="0", column="1")

#Druhé číslo - Vytvoření layoutu a zarovnání do mřížky(gridu).
label_number_2 = tkinter.Label(window, text="Enter second number: ")
label_number_2.grid(row="1", column="0")
value_number_2 = tkinter.Entry(window)
value_number_2.grid(row="1", column="1")

#Dropdown menu - Vytvoření layoutu a zarovnání do mřížky(gridu).
label_select_operations = tkinter.Label(window, text="Select operations: ",borderwidth=2, relief="groove")
label_select_operations.grid(row="2", column="0")

dropdown_placeholder = tkinter.StringVar(window)
dropdown_placeholder.set("Select by clicking")
menu = tkinter.OptionMenu(window, dropdown_placeholder, "Add","Subtract", "Multiply", "Divide")
menu.config(activeforeground='red')
menu.grid(row="3", column="0")

#Hlavní logika sčítání
def compute():
    num_1 = float(value_number_1.get())
    num_2 = float(value_number_2.get())

    if dropdown_placeholder.get() == "Add":
        result = num_1 + num_2

    elif dropdown_placeholder.get() == "Subtract":
        result = num_1 - num_2

    elif dropdown_placeholder.get() == "Multiply":
        result = num_1 * num_2

    elif dropdown_placeholder.get() == "Divide":
        result = num_1 / num_2

    else:
        result = "Select operation."

    text_area = tkinter.Text(master=window, width=20, height=2)
    text_area.grid(row=4, column=1)
    text_area.insert(tkinter.END, result)

button = tkinter.Button(window, text="Submit", command=compute, bg="lightgreen")
button.grid(row="3", column="1")

#Hlavní loop, který se pořád obnovuje a nčítá nové požadavky.
window.mainloop()