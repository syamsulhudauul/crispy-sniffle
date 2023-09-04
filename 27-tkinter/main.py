from  tkinter import Tk,Button,Label,Entry,Radiobutton,IntVar

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

my_label = Label(text="is equal to", font=("Arial", 24))
my_label.grid(column=0, row=1)

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)

ans_label = Label(text="0", font=("Arial", 24))
ans_label.grid(column=1, row=1)

def button_clicked():
    mile = float(input.get())
    km = mile * 1.60934
    ans_label.config(text=km)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

km_label = Label(text="Km", font=("Arial", 24))
km_label.grid(column=2, row=1)

mile_label = Label(text="Miles", font=("Arial", 24))
mile_label.grid(column=2, row=0)

window.mainloop()