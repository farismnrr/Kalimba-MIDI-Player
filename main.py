import os
from mido import MidiFile
import keyboard
import argparse
from tkinter import Tk, filedialog
import time

class MidiPlayer:
    def __init__(self):
        self.play_state = 'idle'
        self.octave_interval = 12
        self.c3_pitch = 48
        self.c5_pitch = 72
        self.b5_pitch = 83
        self.keytable = "z?x?cv?b?n?m" + "a?s?df?g?h?j" + "q?w?er?t?y?u"
        self.notetable = "C?D?EF?G?A?B"

    def note_name(self, pitch):
        pitch_index = pitch % self.octave_interval
        if pitch_index < 0:
            return '-'
        pre = self.notetable[pitch_index]
        if pre == '?':
            pre = self.notetable[pitch_index - 1] + '#'
        return pre + str(pitch // self.octave_interval - 1)

    def midi_playable(self, event):
        if event.is_meta or event.type != 'note_on':
            return False
        return True

    def find_best_shift(self, midi_data):
        note_counter = [0] * self.octave_interval
        octave_list = [0] * 11

        for event in midi_data:
            if not self.midi_playable(event):
                continue

            for i in range(self.octave_interval):
                note_pitch = (event.note + i) % self.octave_interval
                if self.keytable[note_pitch] != '?':
                    note_counter[i] += 1
                    note_octave = (event.note + i) // self.octave_interval
                    octave_list[note_octave] += 1

        max_note = max(range(len(note_counter)), key=note_counter.__getitem__)
        shifting = 0
        counter = 0

        for i in range(len(octave_list) - 3):
            amount = sum(octave_list[i: i + 3])

            if amount > counter:
                counter = amount
                shifting = i

        return int(max_note + (4 - shifting) * (self.octave_interval - 12))

    def play(self, midi, shifting):
        self.play_state = 'playing'  # Initialize play_state as 'playing'
        print('Mulai memainkan')

        for event in midi:
            if self.play_state != 'playing':  # Use self.play_state here
                break

            time.sleep(event.time)

            if not self.midi_playable(event):
                continue

            pitch = event.note + shifting
            original_pitch = pitch

            if pitch < self.c3_pitch:
                print(f"Pitch {self.note_name(pitch)} lebih rendah dari C3")
                pitch = pitch % self.octave_interval + self.c3_pitch

            elif pitch > self.b5_pitch:
                print(f"Pitch {self.note_name(pitch)} lebih tinggi dari B5")
                pitch = pitch % self.octave_interval + self.c5_pitch

            if pitch < self.c3_pitch or pitch > self.b5_pitch:
                print('lewati catatan ini')
                continue

            key_press = self.keytable[pitch - self.c3_pitch]
            print(
                f"Kunci asli: {self.note_name(original_pitch)}({original_pitch}) Kunci main: {self.note_name(pitch)}({pitch}) Tekan: {key_press.upper()}\n")
            keyboard.send(key_press)

    def control(self, *args):
        if self.play_state == 'playing':
            self.play_state = 'pause'

        elif self.play_state == 'pause':
            self.play_state = 'playing'

        elif self.play_state == 'idle':
            self.play_state = 'playing'
            keyboard.call_later(self.play, args=args, delay=1)

    def main(self):
        parser = argparse.ArgumentParser(
            description='Pemutar otomatis file MIDI dengan Keylimba')
        parser.add_argument('midi', nargs="?", type=str, help='path ke file MIDI')
        args = parser.parse_args()

        midi = args.midi

        if not midi:
            root = Tk()
            root.withdraw()
            midi = filedialog.askopenfilename(title='Pilih file MIDI', filetypes=[('File MIDI', '*.mid')])
            root.destroy()

        if not os.path.exists(midi):
            print(f"Error: File MIDI '{midi}' yang ditentukan tidak ada.")
            exit(1)

        midi = MidiFile(midi)
        shifting = self.find_best_shift(midi)

        print("Tekan ' ' untuk memainkan/jeda, dan tekan 'esc' untuk keluar.\n")
        keyboard.add_hotkey(' ', lambda: self.control(midi, shifting),
                            suppress=True, trigger_on_release=True)
        keyboard.wait('esc', suppress=True)
        self.play_state = 'idle'

if __name__ == '__main__':
    player = MidiPlayer()
    player.main()