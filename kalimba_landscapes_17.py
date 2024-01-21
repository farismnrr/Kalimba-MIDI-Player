import pyautogui
import keyboard
import threading

# Koordinat titik yang akan diklik
Note_C4 = (957,566)
Note_D4 = (854, 538)
Note_E4 = (1075, 512)
Note_F4 = (731, 472)
Note_G4 = (1186, 474)
Note_A4 = (615, 444)
Note_B4 = (1297, 429)

Note_C5 = (502, 424)
Note_D5 = (1410, 401)
Note_E5 = (388, 385)
Note_F5 = (1525, 385)
Note_G5 = (277, 374)
Note_A5 = (1634, 357)
Note_B5 = (171, 350)

Note_C6 = (1748, 338)
Note_D6 = (45, 348)
Note_E6 = (1860, 327)

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
        # Tambahkan hotkey lain di sini
    }

    if event.name in key_to_coordinate:
        coordinate = key_to_coordinate[event.name]
        t = threading.Thread(target=klik_koordinat, args=coordinate)
        t.start()

keyboard.on_press(check_key_press)
keyboard.wait('esc')