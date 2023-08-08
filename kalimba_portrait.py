import pyautogui
import keyboard

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

# Mengikat fungsi check_key_press ke setiap kejadian keyboard
keyboard.on_press(check_key_press)
keyboard.wait('esc')
