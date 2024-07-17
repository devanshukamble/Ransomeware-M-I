# working
import os
import win32api
from cryptography import fernet
import ctypes
import datetime
 
# creating a time object to count time
time1 = datetime.datetime.now()
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

# img = r"D:\\wallpaper.jpg"
# ctypes.windll.user32.SystemParametersInfoW(20,0,img,0)
# os.remove("wallpaper.jpg")

time2 = datetime.datetime.now()
print("Time Taken to encrypt all files",(time2-time1).total_seconds())