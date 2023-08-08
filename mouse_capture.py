import tkinter as tk
from tkinter import ttk
import pyautogui

def get_mouse_position():
    global capture_count
    if capture_count <= 100:
        position = pyautogui.position()
        pos_label.config(text=f"Mouse Position: {position}")
        if capture_count > 0:
            capture_list.insert("", tk.END, values=(capture_count, position))
            captured_positions.append(position)
            capture_count += 1
            capture_list.yview_moveto(1.0)  # Melakukan scroll ke posisi terbaru

def capture_mouse_position(event):
    if event.char == "c" and capture_count <= 100:
        captured_positions.append(pyautogui.position())
        update_capture_list()

def reset_capture_list():
    global capture_count
    capture_count = 1
    captured_positions.clear()
    for i in capture_list.get_children():
        capture_list.delete(i)

def update_capture_list():
    capture_list.delete(*capture_list.get_children())
    for i, position in enumerate(captured_positions):
        capture_list.insert("", tk.END, values=(i+1, position))
    capture_list.yview_moveto(1.0)  # Melakukan scroll ke posisi terbaru

def save_to_text():
    file_path = "capture_data.txt"
    with open(file_path, "w") as file:
        for position in captured_positions:
            file.write(f"{position.x}, {position.y}\n")
    print(f"Data capture berhasil disimpan ke dalam file: {file_path}")

# Membuat window tkinter
window = tk.Tk()
window.title("Mouse Position Tracker")

# Membuat frame utama
main_frame = ttk.Frame(window, padding="20")
main_frame.grid(row=0, column=0, sticky="nsew")

# Membuat label untuk menampilkan posisi kursor mouse
pos_label = ttk.Label(main_frame, text="Press 'c' to capture the mouse position")
pos_label.grid(row=0, column=0, sticky="w", pady=10)

# Membuat tombol reset untuk menghapus hasil capture
reset_button = ttk.Button(main_frame, text="Reset", command=reset_capture_list)
reset_button.grid(row=2, column=0, pady=10)

# Membuat tombol save untuk menyimpan hasil capture ke dalam file teks
save_button = ttk.Button(main_frame, text="Save", command=save_to_text)
save_button.grid(row=3, column=0, pady=10)

# Membuat Treeview untuk menampilkan hasil capture dengan scrollbar
tree_frame = ttk.Frame(main_frame)
tree_frame.grid(row=4, column=0, pady=10)

scrollbar = ttk.Scrollbar(tree_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

capture_list = ttk.Treeview(tree_frame, columns=("No.", "Position"), show="headings", selectmode="browse", yscrollcommand=scrollbar.set)
capture_list.pack()

scrollbar.config(command=capture_list.yview)

capture_list.heading("No.", text="No.")
capture_list.column("No.", width=50, anchor="center")
capture_list.heading("Position", text="Position")
capture_list.column("Position", width=200)

# Menambahkan event handler untuk menangkap lokasi mouse saat tombol "c" ditekan
captured_positions = []
capture_count = 1
window.bind("<Key>", capture_mouse_position)

# Menjalankan event loop tkinter
window.mainloop()
