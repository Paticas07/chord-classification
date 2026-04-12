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

@dataclass
class Note:
    base: int
    total_value: int

@dataclass
class Chord:
    root: Note
    third:Note
    fifth: Note