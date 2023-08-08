import subprocess
import tkinter as tk
from tkinter import ttk
import keyboard
import argparse
import importlib
from main import MidiPlayer
import textwrap

def install_module(module_name):
    try:
        importlib.import_module(module_name)
        print(f"Modul {module_name} telah terinstal.")
    except ImportError:
        print(f"Memulai instalasi {module_name}...")
        subprocess.Popen(['pip', 'install', module_name])
        print(f"Instalasi {module_name} sedang berjalan.")

# Cek dan instal modul mido
install_module('mido')

# Cek dan instal modul keyboard
install_module('keyboard')

# Cek dan instal modul pyautogui
install_module('pyautogui')

# Cek dan instal modul argparse
install_module('argparse')

def interupt():
    try:
        keyboard.wait('esc')
    except KeyboardInterrupt:
        pass
    finally:
        keyboard.unhook_all()

def midi_player_keyboard():
    print("MIDI Player Keyboard")
    hotkey_process = subprocess.Popen(['python', 'kalimba_landscapes.py'])
    interupt()

def kalimba_full():
    print("Kalimba Landscape")
    hotkey_process = subprocess.Popen(['python', 'kalimba_landscapes.py'])
    player = MidiPlayer()
    player.main()
    interupt()

def kalimba_short():
    print("Kalimba Portrait")
    hotkey_process = subprocess.Popen(['python', 'kalimba_portrait.py'])
    player = MidiPlayer()
    player.main()
    interupt()

def kalimba_main():
    print("MIDI Controller with Keyboard")
    player = MidiPlayer()
    player.main()
    interupt()

def kalimba_number():
    print("Hotkey with Number")
    hotkey_process = subprocess.Popen(['python', 'kalimba_numbers.py'])
    interupt()

def switch_menu(option):
    if option == "Keylimba Hotkey":
        midi_player_keyboard()
    elif option == "Kalimba Landscape":
        kalimba_full()
    elif option == "Kalimba Portrait":
        kalimba_short()
    elif option == "MIDI Controller with Keyboard":
        kalimba_main()
    elif option == "Hotkey with Number":
        kalimba_number()
    else:
        print("Invalid menu option")

def main_menu():
    root = tk.Tk()
    root.title("Kalimba Player App")

    # Set the window size to match iPhone 13 dimensions
    iphone_width = 500
    iphone_height = 300
    root.geometry(f"{iphone_width}x{iphone_height}")

    main_label = tk.Label(
        root,
        text="Main Menu",
        font=("Helvetica", 16, "bold"),  # Apply bold font
        foreground="#007BFF",  # Apply primary color
    )
    main_label.pack(pady=20)

    button_width = 30
    button_height = 2  # Adjust the height of the button as needed

    style = ttk.Style()
    style.configure(
        "Primary.TButton",
        background="#007BFF",
        foreground="#007BFF",
        font=("Helvetica", 12, "bold"),
        width=button_width,  # Set the button width using the variable
        height=button_height  # Set the button height using the variable
    )

    button_texts = [
        "Keylimba Hotkey",
        "Kalimba Landscape",
        "Kalimba Portrait",
        "MIDI Controller with Keyboard",
        "Hotkey with Number"
    ]

    for text in button_texts:
        wrapped_text = textwrap.fill(text, width=button_width)
        menu_button = ttk.Button(
            root,
            text=wrapped_text,
            command=lambda t=text: switch_menu(t),
            style="Primary.TButton"
        )
        menu_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
