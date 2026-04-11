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
LEN_SCALE = 12

IM3 = 1
Im3 = 2
IM2 = 3
IP4 = 4

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

def interval(n1:note,n2:note) -> int:
    if n1.total_value > n2.total_value:
        n2.total_value += LEN_SCALE
    return n2.total_value - n1.total_value
