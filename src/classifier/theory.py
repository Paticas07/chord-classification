from .models import *

def get_note(raw_note:str) -> Note:
    args = list(raw_note)
    base = NOTES[args[0].upper()]
    elem = len(args)

    t_value = base
    for i in range (elem-1):
        if args[i+1] == '#':
            t_value += SHARP
        elif args[i+1] == 'b':
            t_value += FLAT

    nota = Note(base, t_value % 12)

    return nota

def interval(n1:Note,n2:Note) -> int:
    if n1.total_value > n2.total_value:
        n2.total_value += LEN_SCALE
    return n2.total_value - n1.total_value
