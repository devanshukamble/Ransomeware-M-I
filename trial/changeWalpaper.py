img = r"D:\om.jpg"
import ctypes
ctypes.windll.user32.SystemParametersInfoW(20,0,img,0)