import time
from pynput import keyboard

def on_presss(key):
    try:
        if key == keyboard.Key.esc:
            print("Exiting...")
            return False
        else:
            print(f"key {key.char} pressed")
    except AttributeError:
        print(f'Special key {key} pressed')

def on_releasee(key):
    print(f"exit{key}")

lt = time.localtime()
localtime_year = lt.tm_year
localtime_month = lt.tm_mon
localtime_day = lt.tm_mday


while True:
    try:
        dob = input("Enter your D.O.B: ")
        check_dob = dob.strip().split('/')
        day = check_dob[0]
        month = check_dob[1]
        year = check_dob[2]
        age_years = localtime_year - int(year)
        age_month = localtime_month - int(month)
        age_day = localtime_day - int(day)
        print(f"You are {age_years} years, {age_month} months, and {age_day} days old")
        print("")
        print("press Esc to exit")
        with keyboard.Listener(on_press=on_presss, on_release=on_releasee) as l:
            l.join()

    except IndexError:
        print("Incorrect! Please input using '-'\n"
              "Example: 20-7-1999")
        print("")

