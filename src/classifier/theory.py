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
    cnt = 0
    acc_string = ''
    t_value = base

    
    for i in range (elem-1):
        cnt +=1
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

        else:
            print(f"Error: {i} is not a valid accident please use # or b.")
            sys.exit(1)            
        acc_string = args[1] * (cnt)

    nota = Note(base, t_value % 12,acc_string)

    return nota

def interval(n1:Note,n2:Note) -> int:

    base1 = n1.base
    base2 = n2.base
    if base1 > base2:
        base2 += LEN_SCALE
    if base1 in [0,5,7]:
        i = 4
    else:
        i = 3
    
    if base2 - base1 != i:
        print(f"Error: interval formed by {VAL_NOTES[n1.base]} and {VAL_NOTES[n2.base]} not valid.")
        print(f"Interval is not a third.")
        sys.exit(1)

    if n1.total_value > n2.total_value:
        n2.total_value += LEN_SCALE
    interval = n2.total_value - n1.total_value

    if (interval != 3 and interval != 4):
        print(f"Error: interval formed by {VAL_NOTES[n1.base]} and {VAL_NOTES[n2.base]} not valid.")
        sys.exit(1)
    return interval

def interval_chord(c:Chord) -> tuple:
    return (interval(c.root,c.third), interval(c.third,c.fifth))