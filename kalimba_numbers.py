import pyautogui
import keyboard
import threading

# Koordinat titik yang akan diklik
Note_C5 = (583, 410)
Note_D5 = (1328, 381)
Note_E5 = (501, 363)
Note_F5 = (1410, 358)
Note_G5 = (417, 353)
Note_A5 = (1512, 339)
Note_B5 = (323, 321)

Note_C6 = (1598, 314)
Note_D6 = (222, 303)
Note_E6 = (1686, 298)

# Fungsi untuk mengklik koordinat tertentu
def klik_koordinat(x, y):
    pyautogui.click(x, y)

# Fungsi untuk mengaktifkan klik koordinat saat hotkey tertentu ditekan
def check_key_press(event):
    key_to_coordinate = {
        # Map hotkeys to coordinates
        '1': Note_C5,
        '2': Note_D5,
        '3': Note_E5,
        '4': Note_F5,
        '5': Note_G5,
        '6': Note_A5,
        '7': Note_B5,
        
        '8': Note_C6,
        '9': Note_D6,
        '0': Note_E6,
        # Tambahkan hotkey lain di sini
    }
    
    if event.name in key_to_coordinate:
        coordinate = key_to_coordinate[event.name]
        t = threading.Thread(target=klik_koordinat, args=coordinate)
        t.start()

keyboard.on_press(check_key_press)
keyboard.wait('esc')