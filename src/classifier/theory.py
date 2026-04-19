from classifier.models import *
import sys

def get_note(raw_note:str) -> Note:
    args = list(raw_note)
    if args[0].upper()  not in NOTES:
        print(f"ERROR: {raw_note} is not a valid note.")
        print("Please enter a valid pitch (A-G).")
        sys.exit(1)

    base = NOTES[args[0].upper()]
    elem = len(args)
    status = 0

    t_value = base
    for i in range (elem-1):
        if args[i+1] == '#':
            if (status == FLAT):
                print(f"Error: {raw_note} is not a valid note.")
                print("Please use only # or b, do not use both.")
                sys.exit(1)

            status = SHARP
            t_value += SHARP
        elif args[i+1] == 'b':
            if (status == SHARP):
                print(f"Error: {raw_note} is not a valid note.")
                print("Please use only # or b, do not use both.")
                sys.exit(1)

            status = FLAT
            t_value += FLAT

    nota = Note(base, t_value % 12)

    return nota

def interval(n1:Note,n2:Note) -> int:
    if n1.total_value > n2.total_value:
        n2.total_value += LEN_SCALE
    interval = n2.total_value - n1.total_value

    if (interval != 3 and interval != 4):
        print(f"Error: interval formed by {VAL_NOTES[n1.base]} and {VAL_NOTES[n2.base]} not valid.")
        sys.exit(1)
    return interval

def interval_chord(c:Chord) -> tuple:
    return (interval(c.root,c.third), interval(c.third,c.fifth))