# working
import os
import win32api
from cryptography import fernet
os.chdir("D:\BE\SEM 3\Python_indi")
key = ''
with open('key.key','rb') as f1:
    key = f1.read()
fer = fernet.Fernet(key)
for i in os.walk("D:\BE\SEM 3\Python_indi"):
    for j in i[2]:
        if j.endswith('.txt'):
            file_path = os.path.join(i[0], j)
            s = ""
            try:
                with open(file_path, 'rb') as f:
                    s = f.read()
                s = fer.decrypt(s)
                s = s.decode("ascii")
                with open(file_path,'w') as f1:
                    f1.write(s)
                print(f'{j}.txt decryped')
            except Exception as e:
                print(f"Error decrypting {file_path}: {e}")
        if j.endswith('.png') or j.endswith('.jpg') or j.endswith('.gif') or j.endswith('.jpeg'):
            file_path = os.path.join(i[0], j)
            s = ""
            try:
                with open(file_path, 'rb') as f:
                    s = f.read()
                s = fer.decrypt(s)
                with open(file_path,'wb') as f1:
                    f1.write(s)
                print(f'{j}.img decryped')
            except Exception as e:
                print(f"Error decrypting {file_path}: {e}")
os.remove('key.key')