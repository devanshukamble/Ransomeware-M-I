import ctypes
import shutil
import os

# Function to get the path of the wallpaper image
def get_wallpaper_path():
    SPI_GETDESKWALLPAPER = 0x73
    MAX_PATH = 260
    wallpaper_path_buffer = ctypes.create_unicode_buffer(MAX_PATH)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, MAX_PATH, wallpaper_path_buffer, 0)
    return wallpaper_path_buffer.value

# Get the path of the wallpaper image
wallpaper_path = get_wallpaper_path()

if wallpaper_path:
    # Define the destination folder
    destination_folder = r"D:\BE\SEM 3\Python_indi"  # Using raw string to avoid escaping backslashes
    
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)
    
    # Define the destination file path
    destination_file = os.path.join(destination_folder, "wallpaper.jpg")
    
    # Copy the wallpaper to the destination folder with the new name
    shutil.copy(wallpaper_path, destination_file)
    
    print("Wallpaper copied successfully!")

    # Set the copied wallpaper as the desktop wallpaper
    # ctypes.windll.user32.SystemParametersInfoW(20, 0, destination_file, 0x02)  # 0x02 is SPIF_SENDCHANGE
else:
    print("Failed to get wallpaper path.")
