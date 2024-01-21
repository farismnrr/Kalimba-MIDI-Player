import pyautogui
import keyboard
import threading

# Koordinat titik yang akan diklik
Note_C4 = (539, 1048)
Note_D4 = (490, 1021)
Note_E4 = (593, 997)
Note_F4 = (436, 977)
Note_G4 = (638, 957)
Note_A4 = (383, 936)
Note_B4 = (688, 921)

Note_C5 = (335, 913)
Note_D5 = (743, 902)
Note_E5 = (283, 889)
Note_F5 = (795, 880)
Note_G5 = (233, 873)
Note_A5 = (842, 862)
Note_B5 = (182, 846)

Note_C6 = (895, 846)
Note_D6 = (133, 831)
Note_E6 = (949, 828)
Note_F6 = (79, 823)
Note_G6 = (996, 823)
Note_A6 = (29, 815)
Note_B6 = (1048, 816)

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