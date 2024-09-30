# -*- coding: utf-8 -*-
from jackit import keymap


class DuckyParser:
    ''' Help map ducky-like script to HID codes to be sent '''

    hid_map = {
        '':           [0, 0],
        'ALT':        [0, 4],
        'SHIFT':      [0, 2],
        'CTRL':       [0, 1],
        'GUI':        [0, 8],
        'SCROLLLOCK': [71, 0],
        'ENTER':      [40, 0],
        'F12':        [69, 0],
        'HOME':       [74, 0],
        'F10':        [67, 0],
        'F9':         [66, 0],
        'ESCAPE':     [41, 0],
        'PAGEUP':     [75, 0],
        'TAB':        [43, 0],
        'PRINTSCREEN': [70, 0],
        'F2':         [59, 0],
        'CAPSLOCK':   [57, 0],
        'F1':         [58, 0],
        'F4':         [61, 0],
        'F6':         [63, 0],
        'F8':         [65, 0],
        'DOWNARROW':  [81, 0],
        'DELETE':     [42, 0],
        'RIGHT':      [79, 0],
        'F3':         [60, 0],
        'DOWN':       [81, 0],
        'DEL':        [76, 0],
        'END':        [77, 0],
        'INSERT':     [73, 0],
        'F5':         [62, 0],
        'LEFTARROW':  [80, 0],
        'RIGHTARROW': [79, 0],
        'PAGEDOWN':   [78, 0],
        'PAUSE':      [72, 0],
        'SPACE':      [44, 0],
        'UPARROW':    [82, 0],
        'F11':        [68, 0],
        'F7':         [64, 0],
        'UP':         [82, 0],
        'LEFT':       [80, 0]
    }

    blank_entry = {
        "mod": 0,
        "hid": 0,
        "char": '',
        "sleep": 0
    }

    def __init__(self, attack_script, layout=None):
        key_mapping = keymap.mapping.get(layout, keymap.mapping['us'])
        self.hid_map.update(key_mapping)
        self.script = attack_script.split("\n")

    def char_to_hid(self, char):
        return self.hid_map.get(char, [0, 0])

    def parse(self):
        entries = []

        # process lines for repeat
        for pos, line in enumerate(self.script):
            if line.startswith("REPEAT"):
                self.script.remove(line)
                for i in range(1, int(line.split()[1])):
                    self.script.insert(pos, self.script[pos - 1])

        for line in self.script:
            entry = self.blank_entry.copy()
            if line.startswith('ALT'):
                entry['char'] = line.split()[1] if ' ' in line else ''
                entry['hid'], mod = self.char_to_hid(entry['char'])
                entry['mod'] = 4 | mod
                entries.append(entry)

            elif line.startswith(("GUI", "WINDOWS", "COMMAND")):
                entry['char'] = line.split()[1] if ' ' in line else ''
                entry['hid'], mod = self.char_to_hid(entry['char'])
                entry['mod'] = 8 | mod
                entries.append(entry)

            elif line.startswith(("CTRL-ALT", "CONTROL-ALT")):
                entry['char'] = line.split()[1] if ' ' in line else ''
                entry['hid'], mod = self.char_to_hid(entry['char'])
                entry['mod'] = 4 | 1 | mod
                entries.append(entry)

            elif line.startswith(("CTRL-SHIFT", "CONTROL-SHIFT")):
                entry['char'] = line.split()[1] if ' ' in line else ''
                entry['hid'], mod = self.char_to_hid(entry['char'])
                entry['mod'] = 4 | 2 | mod
                entries.append(entry)

            elif line.startswith(("CTRL", "CONTROL")):
                entry['char'] = line.split()[1] if ' ' in line else ''
                entry['hid'], mod = self.char_to_hid(entry['char'])
                entry['mod'] = 1 | mod
                entries.append(entry)

            elif line.startswith("SHIFT"):
                entry['char'] = line.split()[1] if ' ' in line else ''
                entry['hid'], mod = self.char_to_hid(entry['char'])
                entry['mod'] = 2 | mod
                entries.append(entry)

            elif line.startswith(("ESC", "APP", "ESCAPE")):
                entry['char'] = "ESC"
                entry['hid'], entry['mod'] = self.char_to_hid('ESCAPE')
                entries.append(entry)

            elif line.startswith("DELAY"):
                entry['sleep'] = line.split()[1]
                entries.append(entry)

            elif line.startswith("STRING"):
                for char in " ".join(line.split()[1:]):
                    entry = self.blank_entry.copy()
                    entry['char'] = char
                    entry['hid'], entry['mod'] = self.char_to_hid(char)
                    entries.append(entry)

            elif line.startswith("ENTER"):
                entry['char'] = "\n"
                entry['hid'], entry['mod'] = self.char_to_hid('ENTER')
                entries.append(entry)

            # arrow keys
            elif line.startswith(("UP", "UPARROW")):
                entry['char'] = "UP"
                entry['hid'], entry['mod'] = self.char_to_hid('UP')
                entries.append(entry)

            elif line.startswith(("DOWN", "DOWNARROW")):
                entry['char'] = "DOWN"
                entry['hid'], entry['mod'] = self.char_to_hid('DOWN')
                entries.append(entry)

            elif line.startswith(("LEFT", "LEFTARROW")):
                entry['char'] = "LEFT"
                entry['hid'], entry['mod'] = self.char_to_hid('LEFT')
                entries.append(entry)

            elif line.startswith(("RIGHT", "RIGHTARROW")):
                entry['char'] = "RIGHT"
                entry['hid'], entry['mod'] = self.char_to_hid('RIGHT')
                entries.append(entry)

            elif not line.strip():
                continue  # skip empty lines

            else:
                print(f"CAN'T PROCESS... {line}")

        return entries

