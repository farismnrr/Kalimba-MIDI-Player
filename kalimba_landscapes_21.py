import pyautogui
import keyboard
import threading

# Koordinat titik yang akan diklik
Note_C4 = (956, 579)
Note_D4 = (856, 505)
Note_E4 = (1051, 506)
Note_F4 = (781, 464)
Note_G4 = (1145, 428)
Note_A4 = (680, 434)
Note_B4 = (1230, 400)

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
Note_F6 = (131, 310)
Note_G6 = (1774, 297)
Note_A6 = (39, 284)
Note_B6 = (1876, 289)

# Fungsi untuk mengklik koordinat tertentu
def klik_koordinat(x, y):
    pyautogui.click(x, y)

# Fungsi untuk mengaktifkan klik koordinat saat hotkey tertentu ditekan
def check_key_press(event):
    key_to_coordinate = {
        # Map hotkeys to coordinates
        'z': Note_C4,
        'x': Note_D4,
        'c': Note_E4,
        'v': Note_F4,
        'b': Note_G4,
        'n': Note_A4,
        'm': Note_B4,
        
        'a': Note_C5,
        's': Note_D5,
        'd': Note_E5,
        'f': Note_F5,
        'g': Note_G5,
        'h': Note_A5,
        'j': Note_B5,
        
        'q': Note_C6,
        'w': Note_D6,
        'e': Note_E6,
        'r': Note_F6,
        't': Note_G6,
        'y': Note_A6,
        'u': Note_B6,
        # Tambahkan hotkey lain di sini
    }

    if event.name in key_to_coordinate:
        coordinate = key_to_coordinate[event.name]
        t = threading.Thread(target=klik_koordinat, args=coordinate)
        t.start()

keyboard.on_press(check_key_press)
keyboard.wait('esc')