import time
from tkinter import *
from tkinter import messagebox
import sys

# Create the interface object
clockWindow = Tk()
clockWindow.geometry("1920x1080")
clockWindow.title("Countdown Timer")
clockWindow.configure(background='#fff')

# Declare variables
hourString = StringVar()
minuteString = StringVar()
secondString = StringVar()
dataString = StringVar()

# Set strings to default value
hourString.set("24")
minuteString.set("00")
secondString.set("00")

# Get user input
main_title = Label(clockWindow, text="Your files are encrypted",
                   font=("Calibri", 30, "bold"), bg="#fff")
main_title.place(x=550, y=10)

warning = Label(clockWindow, text="To get the key to decrypt files,you have to pay ", font=(
    "Calibri", 15, ""), bg="#fff")
warning.place(x=400, y=100)

warning1 = Label(clockWindow, text=" 6.9 million USD ",
                 font=("Calibri", 15, ""), bg="#fff", fg="red")
warning1.place(x=790, y=100)

warning2 = Label(clockWindow, text="if payment is not made",
                 font=("Calibri", 15, ""), bg="#fff")
warning2.place(x=930, y=100)

warning3 = Label(clockWindow, text="Your all data will be ",
                 font=("Calibri", 15, ""), bg="#fff")
warning3.place(x=630, y=130)

warning4 = Label(clockWindow, text="erased", font=(
    "Calibri", 15, ""), bg="#fff", fg="red")
warning4.place(x=805, y=130)

warning5 = Label(clockWindow, text="More instructions forthcoming. -fsociety.",
                 font=("Calibri", 15, ""), bg="#fff")
warning5.place(x=580, y=160)

time_title = Label(clockWindow, text="Time left : ",
                   font=("Calibri", 40, ""), bg="#fff")
hourTextbox = Label(clockWindow, width=3, font=(
    "Calibri", 40, ""), textvariable=hourString, bg='#fff', fg='red')
col1 = Label(clockWindow, width=2, font=(
    "Calibri", 40, ""), text="H", bg="#fff")
minuteTextbox = Label(clockWindow, width=3, font=(
    "Calibri", 40, ""), textvariable=minuteString, bg='#fff', fg='red')
col2 = Label(clockWindow, width=2, font=(
    "Calibri", 40, ""), text="m", bg="#fff")
secondTextbox = Label(clockWindow, width=3, font=(
    "Calibri", 40, ""), textvariable=secondString, bg='#fff', fg='red')
col3 = Label(clockWindow, width=2, font=(
    "Calibri", 40, ""), text="s", bg="#fff")
dataTextbox = Entry(clockWindow, width=20, font=(
    "Calibri", 20, ""), textvariable=dataString, bg="#B6D0E2")
# Center textboxes
time_title.place(x=430, y=280)
hourTextbox.place(x=650, y=280)
col1.place(x=720, y=280)
minuteTextbox.place(x=765, y=280)
col2.place(x=840, y=280)
secondTextbox.place(x=890, y=280)
col3.place(x=960, y=280)
dataTextbox.place(x=600, y=380)
# paymentButton.place(x=650,y=420)


def runTimer():
    try:
        clockTime = int(hourString.get())*3600 + \
            int(minuteString.get())*60 + int(secondString.get())
    except:
        print("Incorrect values")

    while (clockTime > -1):
        flag = False

        totalMinutes, totalSeconds = divmod(clockTime, 60)

        totalHours = 0
        if (totalMinutes > 60):
            totalHours, totalMinutes = divmod(totalMinutes, 60)

        hourString.set("{0:2d}".format(totalHours))
        minuteString.set("{0:2d}".format(totalMinutes))
        secondString.set("{0:2d}".format(totalSeconds))
        if dataString.get() == '10':
            flag = True
            sucess = Label(clockWindow, text='Your files will be decrypted soon...', font=("Calibri", 35, ""), bg="#fff",fg="green")
            sucess.place(x=400, y=460)
            break
        # if flag:
        #     time.sleep(2)
        #     sys.exit()
        # Update the interface
        clockWindow.update()
        time.sleep(0.9)
        # Let the user know if the timer has expired
        if (clockTime == 0):
            pass
            # messagebox.showinfo("", "Sorry All Files Deleted")
        clockTime -= 1

runTimer()
# Keep looping
clockWindow.mainloop()
