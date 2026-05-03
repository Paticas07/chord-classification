from classifier.models import *
import classifier.models as models
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

def invert_chord(c: Chord):
    temp = c.root
    c.root = c.third
    c.third = c.fifth
    c.fifth = temp

def interval(n1:Note,n2:Note) -> int:
    base1 = n1.base
    base2 = n2.base
    if base1 > base2:
        base2 += LEN_SCALE
    if base1 in [0,5,7]:
        i = 4
    else:
        i = 3
    
    if base2 - base1 != i and models.count == 2 :
        print(f"Error: interval is not a third.")
        sys.exit(1)
    elif base2 - base1 != i:
        return -1


    if n1.total_value > n2.total_value:
        n2.total_value += LEN_SCALE
    interval = n2.total_value - n1.total_value

    if (interval != 3 and interval != 4 and models.count == 2):
        print(f"Error: interval not valid.")
        sys.exit(1)
    elif interval != 3 and interval != 4:
        return -1
    return interval

def interval_chord(c:Chord) -> tuple:
    while interval(c.root,c.third) == -1 or interval(c.third,c.fifth) == -1:
        invert_chord(c)
        models.count = models.count + 1
    return (interval(c.root,c.third), interval(c.third,c.fifth))