import tkinter as tk
import datetime


# functions start
def about():
    about = tk.Tk()
    about.geometry("200x300")
    about.minsize(300, 100)
    about.maxsize(300, 100)
    l = tk.Label(about, text="version: ac1.002\nauthor:\nMd. Mursalatul Islam Pallob", font=("bold", 16),
                 bg="#D35400").pack()
    about.mainloop()


# input functions
# get the inputs from the day month year entry when cleck is clicked

def func_check():
    entry_sec.delete(0, "end")
    entry_min.delete(0, "end")
    entry_hour.delete(0, "end")
    entry_day.delete(0, "end")
    entry_week.delete(0, "end")
    entry_month.delete(0, "end")
    entry_year.delete(0, "end")
    day = int(entry_day_input.get())
    month = int(entry_month_input.get())
    year = int(entry_year_input.get())
    my_birthdate = datetime.datetime(day=day, month=month, year=year)
    current_time = datetime.datetime.now()  # current_time is the time when program is running
    my_days = (current_time.date() - my_birthdate.date()).days
    entry_day.insert(0, my_days)  # output day
    my_years = current_time.year - my_birthdate.year
    entry_year.insert(0, my_years)  # output year
    my_hours = (my_days * 24) + current_time.time().hour
    entry_hour.insert(0, my_hours)  # output hour
    my_mins = (my_hours * 60) + current_time.time().minute
    entry_min.insert(0, my_mins)  # output min
    my_secs = (my_mins * 60) + current_time.time().second
    entry_sec.insert(0, my_secs)  # output second
    my_weeks = my_days // 4
    entry_week.insert(0, my_weeks)
    my_extra_days_after_weeks = my_days % 4
    my_months = my_weeks // 4
    entry_month.insert(0, my_months)
    my_extra_days_after_months = my_weeks % 4
    if my_extra_days_after_weeks != 0:
        if my_extra_days_after_weeks == 1:
            ddddd = "day"
        else:
            ddddd = "days"
        index_of_weeks = len(entry_week.get())
        entry_week.insert(index_of_weeks, f" + {my_extra_days_after_weeks} {ddddd}")
    if my_extra_days_after_months != 0:
        if my_extra_days_after_months == 1:
            dddd = "day"
        else:
            dddd = "days"
        index_of_months = len(entry_month.get())
        entry_month.insert(index_of_months, f" + {my_extra_days_after_months} {dddd}")


def func_clear():
    entry_day_input.delete(0, "end")
    entry_month_input.delete(0, "end")
    entry_year_input.delete(0, "end")


def enter1(*args):
    entry_month_input.focus()


def enter2(*args):
    entry_year_input.focus()


def enter3(*args):
    func_check()


def shift1(*args):
    func_clear()
    entry_day_input.focus()


# functions end
wn = tk.Tk()
wn.geometry("500x600")
wn.minsize(485, 480)
wn.maxsize(485, 480)
wn.configure(bg="#85C1E9")
wn.title("")
wn.iconbitmap("icon1.ico")
# day month year input section
label_empty = tk.Label(wn, text="Age Calculator", font=("bold", 20, "underline"), bg="#85C1E9").grid(rowspan=1,column=2)

label_day_input = tk.Label(wn, bg="#85C1E9", text="Day", font=("bold", 16)).grid(row=2, column=1, padx=55)
entry_day_input = tk.Entry(wn, bg="#D4E6F1", width=7, relief="groove", font="bold")
entry_day_input.focus()
entry_day_input.bind("<Return>", enter1)
entry_day_input.grid(row=3, column=1)

label_month_input = tk.Label(wn, bg="#85C1E9", text="Month", font=("bold", 16)).grid(row=2, column=2, padx=55)
entry_month_input = tk.Entry(wn, bg="#D4E6F1", width=7, relief="groove", font="bold")
entry_month_input.bind("<Return>", enter2)
entry_month_input.grid(row=3, column=2)

label_year_input = tk.Label(wn, bg="#85C1E9", text="Year", font=("bold", 16)).grid(row=2, column=3, padx=55)
entry_year_input = tk.Entry(wn, bg="#D4E6F1", width=7, relief="groove", font="bold")
entry_year_input.bind("<Return>", enter3)
entry_year_input.bind("<Shift_L>", shift1)
entry_year_input.bind("<Shift_R>", shift1)
entry_year_input.grid(row=3, column=3)

label_empty2 = tk.Label(wn, bg="#85C1E9", ).grid(row=5, columnspan=3)

# check clear button section
button_check = tk.Button(wn, bg="#FADBD8", text="CHECK", font=("bold", 18), relief="raised", activeforeground="#52BE80",
                         width=10, command=func_check).grid(row=6, column=1)
button_clear = tk.Button(wn, bg="#FADBD8", text="CLEAR", font=("bold", 18), relief="raised", activeforeground="#E74C3C",
                         width=10, command=func_clear).grid(row=6, column=3)

label_empty3 = tk.Label(wn, bg="#85C1E9", ).grid(row=8, columnspan=3)

# output window
label_sec = tk.Label(wn, bg="#85C1E9", text="sec", font=("bold", 16)).grid(row=9, column=1)
entry_sec = tk.Entry(wn, width=30, relief="raised", font="bold")
entry_sec.grid(row=9, columnspan=4)

label_min = tk.Label(wn, bg="#85C1E9", text="min", font=("bold", 16)).grid(row=10, column=1)
entry_min = tk.Entry(wn, width=30, relief="raised", font="bold")
entry_min.grid(row=10, columnspan=4)

label_hour = tk.Label(wn, bg="#85C1E9", text="hour", font=("bold", 16)).grid(row=11, column=1)
entry_hour = tk.Entry(wn, width=30, relief="raised", font="bold")
entry_hour.grid(row=11, columnspan=4)

label_day = tk.Label(wn, bg="#85C1E9", text="day", font=("bold", 16)).grid(row=12, column=1)
entry_day = tk.Entry(wn, width=30, relief="raised", font="bold")
entry_day.grid(row=12, columnspan=4)

label_week = tk.Label(wn, bg="#85C1E9", text="week", font=("bold", 16)).grid(row=13, column=1)
entry_week = tk.Entry(wn, width=30, relief="raised", font="bold")
entry_week.grid(row=13, columnspan=4)

label_month = tk.Label(wn, bg="#85C1E9", text="month", font=("bold", 16)).grid(row=14, column=1)
entry_month = tk.Entry(wn, width=30, relief="raised", font="bold")
entry_month.grid(row=14, columnspan=4)

label_year = tk.Label(wn, bg="#85C1E9", text="year", font=("bold", 16)).grid(row=15, column=1)
entry_year = tk.Entry(wn, width=30, relief="raised", font="bold")
entry_year.grid(row=15, columnspan=4)

label_empty4 = tk.Label(wn, bg="#85C1E9", ).grid(row=16, columnspan=3)
# about bottun
button_about = tk.Button(wn, text="About", bg="#5499C7", relief="raised", activebackground="#808B96",
                         command=lambda: about()).grid(row=17, column=2)
wn.mainloop()
"""
Version: ac1.002
Author: Md. Mursalatul Islam Pallob
        https://github.com/mursalatulpallob
"""