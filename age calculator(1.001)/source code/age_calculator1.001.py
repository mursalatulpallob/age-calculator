import datetime


def cal():
    # getting birth date as input
    my_birthdate = datetime.datetime(day=int(input("DAY: ")), month=int(input("MONTH: ")), year=int(input("YEAR: ")))
    # data
    weekdayname = ["Monday", "Tuesday", "wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_time = datetime.datetime.now()  # current_time is the time when program is running
    my_days = (current_time.date() - my_birthdate.date()).days
    my_weeks = my_days // 4
    my_extra_days_after_weeks = my_days % 4
    my_months = my_weeks // 4   
    my_extra_days_after_months = my_weeks % 4
    my_years = current_time.year - my_birthdate.year
    my_hours = (my_days * 24) + current_time.time().hour
    my_mins = (my_hours * 60) + current_time.time().minute
    my_secs = (my_mins * 60) + current_time.time().second
    print("\n\nYou were born on: ", weekdayname[my_birthdate.weekday()])
    print("Your Age is now:\n=> ".rjust(16), my_secs, "seconds\n=> ", my_mins, "minutes\n=> ", my_hours, "hours\n=> ",
        my_days,
        "days\n=> ", my_weeks, "weeks", end=" ")
    if my_extra_days_after_weeks != 0:
        if my_extra_days_after_weeks == 1:
            print("+", my_extra_days_after_weeks, "day", end=" ")
        else:
            print("+", my_extra_days_after_weeks, "days", end=" ")
    print("\n=> ", my_months, "months", end=" ")
    if my_extra_days_after_months != 0:
        if my_extra_days_after_months == 1:
            print("+", my_extra_days_after_months, "day", end=" ")
        else:
            print("+", my_extra_days_after_months, "days", end=" ")
    print("\n=> ", my_years, "years\n\n")


# Welcome note
print("\n\n", "!__Welcome to Birth Date Calculator__!".center(80, "_"), "\n")

# finding how many times user wants to run the program
loop = input("Do you want to calculate a few times or a unlimited times?(type \"f\" for few times or \"u\" for "
            "unlimited times\n-> ")
while True:
    if loop != "f" and loop != "u":
        print("Input Error!\nPlease type \"f\" for few times or \"u\" for unlimited times")
        loop = input("-> ")
    else:
        break

if loop == "f":
    loops = input("How many times?\n-> ")
    while True:
        if int(loops):
            break
        else:
            print("Input Error!\nPlease inter a integer number")
            loops = input("-> ")
    print("Now Program will ask you for a day, a month and a year each time to calculate the time.\n As your above"
        " input program will run ", loops, " times")
    for _ in range(int(loops)):
        cal()
elif loop == "u":
    print("Now Program will ask you for a day, a month and a year each time to calculate the time.\n As your above"
        " input program will run unlimited times. You need to close this terminal to exit this program.")
    while True:
        cal()

"""
Version: ac1.001
Author: Md. Mursalatul Islam Pallob
        https://github.com/mursalatulpallob
"""