import subprocess
import tkinter as tk
from tkinter import ttk
import keyboard
from main import MidiPlayer
import textwrap

def interupt():
    try:
        keyboard.wait('esc')
    except KeyboardInterrupt:
        pass
    finally:
        keyboard.unhook_all()

def kalimba_landscape_17():
    print("Kalimba Landscape 17")
    hotkey_process = subprocess.Popen(['python', 'kalimba_landscapes_17.py'])
    player = MidiPlayer()
    player.main()
    interupt()

def kalimba_landscape_21():
    print("Kalimba Landscape 21")
    hotkey_process = subprocess.Popen(['python', 'kalimba_landscapes_21.py'])
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

def switch_menu(option):
    if option == "Kalimba Landscape 17":
        kalimba_landscape_17()
    elif option == "Kalimba Landscape 21":
        kalimba_landscape_21()
    elif option == "Kalimba Portrait":
        kalimba_short()
    elif option == "MIDI Controller with Keyboard":
        kalimba_main()
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
        "Kalimba Landscape 17",
        "Kalimba Landscape 21",
        "Kalimba Portrait",
        "MIDI Controller with Keyboard"
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
