from tkinter import *
PADX = 10
PADY = 10

def miles_to_kilometers():
    miles = float(mile_entry.get())
    kilometers = round(miles * 1.609)
    kilometer_result_label.config(text=f'{kilometers}')

root = Tk()
root.title('Mile to Kilometer')
root.config(padx=PADX, pady=PADY)

mile_entry = Entry(width=8)
mile_entry.grid(row=0, column=1)

miles_label = Label(text='Miles')
miles_label.grid(row=0, column=2, padx=PADX, pady=PADY)

is_equal_label = Label(text='Is equal to: ')
is_equal_label.grid(row=1, column=0)

kilometer_result_label=Label(text='0')
kilometer_result_label.grid(row=1, column=1)

kilometer_label=Label(text='KM')
kilometer_label.grid(row=1, column=2)

calculate_button = Button(text='Calculate', command=miles_to_kilometers)
calculate_button.grid(row=2, column=1, padx=PADX, pady=PADY)














root.mainloop()