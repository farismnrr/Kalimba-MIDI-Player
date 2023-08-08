import pyautogui
import keyboard

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
    if event.name == 'z':
        klik_koordinat(*Note_C4)
    elif event.name == 'x':
        klik_koordinat(*Note_D4)
    elif event.name == 'c':
        klik_koordinat(*Note_E4)
    elif event.name == 'v':
        klik_koordinat(*Note_F4)
    elif event.name == 'b':
        klik_koordinat(*Note_G4)
    elif event.name == 'n':
        klik_koordinat(*Note_A4)
    elif event.name == 'm':
        klik_koordinat(*Note_B4)
            
    elif event.name == 'a':
        klik_koordinat(*Note_C5)
    elif event.name == 's':
        klik_koordinat(*Note_D5)
    elif event.name == 'd':
        klik_koordinat(*Note_E5)
    elif event.name == 'f':
        klik_koordinat(*Note_F5)
    elif event.name == 'g':
        klik_koordinat(*Note_G5)
    elif event.name == 'h':
        klik_koordinat(*Note_A5)
    elif event.name == 'j':
        klik_koordinat(*Note_B5)

    elif event.name == 'q':
        klik_koordinat(*Note_C6)
    elif event.name == 'w':
        klik_koordinat(*Note_D6)
    elif event.name == 'e':
        klik_koordinat(*Note_E6)
    elif event.name == 'r':
        klik_koordinat(*Note_F6)
    elif event.name == 't':
        klik_koordinat(*Note_G6)
    elif event.name == 'y':
        klik_koordinat(*Note_A6)
    elif event.name == 'u':
        klik_koordinat(*Note_B6)
    # Tambahkan hotkey lain di sini
keyboard.on_press(check_key_press)
keyboard.wait('esc')