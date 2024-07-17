# import tkinter as tk
# from tkinter import ttk
# import time

# root = tk.Tk()

# hour_var = tk.StringVar(value='14')
# minute_var = tk.StringVar(value='04')
# second_var = tk.StringVar(value='08')

# # title_lbl = tk.Label(font=('Arial',50),text="Your Files are encrypted")
# time_lbl = tk.Label(font=('Arial',50),text="Time left")
# t_lbl = tk.Label(font=('Arial',50),text=":  ")
# hour_lbl = tk.Label(font=('Arial',50),textvariable=hour_var,fg="red")
# h_lbl = tk.Label(font=('Arial',50),text="H  ")
# minute_lbl = tk.Label(font=('Arial',50),textvariable=minute_var,fg="red")
# m_lbl = tk.Label(font=('Arial',50),text="m  ")
# second_lbl = tk.Label(font=('Arial',50),textvariable=second_var,fg="red")
# s_lbl = tk.Label(font=('Arial',50),text="s")

# time_lbl.grid(column=0,row=0)
# t_lbl.grid(column=1,row=0)
# hour_lbl.grid(column=2,row=0)
# h_lbl.grid(column=3,row=0)
# minute_lbl.grid(column=4,row=0)
# m_lbl.grid(column=5,row=0)
# second_lbl.grid(column=6,row=0)
# s_lbl.grid(column=7,row=0)

# tk.mainloop()
import os
for i in os.walk("D:\\"):
    print(i)