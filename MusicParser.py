class MusicParser:

    def __init__(self):
        self.flat_notes = ['At', 'A', 'Bt', 'B', 'C', 'Dt', 'D', 'Et', 'E', 'F', 'Gt', 'G']
        self.sharp_notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

        self.scale_dict = {
            'Bt': ['Bt', 'C', 'D', 'Et', 'F', 'G', 'A'],
            'C': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
            'G': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
            'D': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
            'A': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
            'E': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
            'B': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'],
            'Gt': ['Gt', 'At', 'Bt', 'B', 'Dt', 'Et', 'F'],
            'Dt': ['Dt', 'Et', 'F', 'Gt', 'At', 'Bt', 'C'],
            'At': ['At', 'Bt', 'C', 'Dt', 'Et', 'F', 'G'],
            'Et': ['Et', 'F', 'G', 'A', 'Bt', 'C', 'D'],
            'F': ['F', 'G', 'A', 'Bt', 'C', 'D', 'E'],
            'A#': ['A#', 'C', 'D', 'D#', 'F', 'G', 'A'],
            'B#': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
            'C#': ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C'],
            'D#': ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D'],
            'E#': ['F', 'G', 'A', 'A#', 'C', 'D', 'E'],
            'F#': ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F'],
            'G#': ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']
        }
        self.rom_dict = {
            'I': '1',
            'II': '2',
            'III': '3',
            'IV': '4',
            'V': '5',
            'VI': '6',
            'VII': '7'
        }
        self.flat = '♭'

    def num_to_note(self, key, num):

        flat = False
        sharp = False

        # Replaces a flat symbol with a more easily workable t
        key = key.replace(self.flat, 't')

        # Weird Cases
        if key == 'D#' and num == 't7':
            return 'C#'
        elif key == 'G#' and num == 't7':
            return 'F#'
        elif key == 'A#' and num == 't7':
            return 'G#'


        # We are fine with blank spaces.
        if num == '' or num == ' ' or num is None:
            return num

        # Convert nines to twos so the list algorithm works.
        if '9' in num:
            num = num.replace('9', '2')

        # Find the number.  It's either in front of the sharp or behind the flat! Or it's just there!
        if '#' in num:
            num = int(num[-1])
            sharp = True
        elif 't' in num:
            num = int(num[-1])
            flat = True
        else:
            num = int(num)

        # Find the note in the key you are in :)
        note = self.scale_dict[key][num - 1]

        ## This Chunk of Code is only if you never want to mess around with keys that "don't exist"
        # except KeyError:
        #     if key == "G#":
        #         note = self.scale_dict['At'][num - 1]
        #     elif key == "C#":
        #         note = self.scale_dict['Dt'][num - 1]
        #     elif key == "D#":
        #         note = self.scale_dict['Et'][num - 1]
        #     elif key == "F#":
        #         note = self.scale_dict['Gt'][num - 1]
        #     elif key == "A#":
        #         note = self.scale_dict['Bt'][num - 1]
        #     elif key == "B#":
        #         note = self.scale_dict['C'][num - 1]

        # Code to try and address when notes should be sharp or flat
        if flat:
            note = note + 't'
        if sharp:
            note = note + '#'

        if note[0] == 't' and note[-1] == 't':
            ref = note[1:]
            if note == 'tAt':
                note = 'G'
            else:
                note = self.flat_notes[self.flat_notes.index(ref) - 1]
        if note[0] == '#' and note[-1] == '#':
            ref = note[1:]
            if note == '#G#':
                note = 'A'
            else:
                note = self.sharp_notes[self.sharp_notes.index(ref) + 1]

        if '##' in note:
            ref = note[:2]
            if note == 'G##':
                note = 'A'
            else:
                note = self.sharp_notes[self.sharp_notes.index(ref) + 1]
        if '#t' in note or 't#' in note:
            note = note[0]

        if note == 'B#':
            note = 'C'
        if note == 'Ct':
            note = 'B'
        if note == 'E#':
            note = 'F'
        if note == 'Ft':
            note = 'E'

        if 't' in note:
            note = note.replace('t', self.flat)

        return note

    def rom_to_key(self, key, rom):
        print(key)
        print(rom)
        if rom == '':
            return key
        elif 't' in rom:
            rom = rom.strip('t')
            num = 't' + self.rom_dict[rom]
        elif '#' in rom:
            rom = rom.strip('#')
            num = '#' + self.rom_dict[rom]
        else:
            num = self.rom_dict[rom]

        new_key = self.num_to_note(key, num)

        return new_key
