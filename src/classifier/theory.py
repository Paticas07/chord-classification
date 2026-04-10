from dataclasses import dataclass

NOTES = {
    'C':0,
    'D':2,
    'E':4,
    'F':5,
    'G':7,
    'A':9,
    'B':11
}

SHARP = 1
FLAT = -1

@dataclass
class note:
    base: int
    total_value: int


def get_note(raw_note:str) -> note:
    args = list(raw_note)
    base = NOTES[args[0].upper()]
    elem = len(args)

    t_value = base
    for i in range (elem-1):
        if args[i+1] == '#':
            t_value += SHARP
        elif args[i+1] == 'b':
            t_value += FLAT

    nota = note(base, t_value % 12)

    return nota
