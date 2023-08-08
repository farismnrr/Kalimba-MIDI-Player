import pyautogui
import keyboard

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
    if event.name == '1':
        klik_koordinat(*Note_C5)
    elif event.name == '2':
        klik_koordinat(*Note_D5)
    elif event.name == '3':
        klik_koordinat(*Note_E5)
    elif event.name == '4':
        klik_koordinat(*Note_F5)
    elif event.name == '5':
        klik_koordinat(*Note_G5)
    elif event.name == '6':
        klik_koordinat(*Note_A5)
    elif event.name == '7':
        klik_koordinat(*Note_B5)

    elif event.name == '8':
        klik_koordinat(*Note_C6)
    elif event.name == '9':
        klik_koordinat(*Note_D6)
    elif event.name == '0':
        klik_koordinat(*Note_E6)
    # Tambahkan hotkey lain di sini
keyboard.on_press(check_key_press)
keyboard.wait('esc')