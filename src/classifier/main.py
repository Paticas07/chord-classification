from .theory import *
from .models import *
import argparse
import sys

def parse_args (input:list) -> Chord:
    notes = [get_note(n) for n in input]
    if len(notes) == 3:
        return Chord(*notes)
    else:
        return None
    
def main ():
    parser = argparse.ArgumentParser(description="Chord Classifier")

    parser.add_argument("notes", nargs=3, help= "Notes of the chord in ascending pitch")
    raw_chord = parser.parse_args()
    chord = parse_args(raw_chord.notes)
    
    if chord:
        print(f"Chord identified: {chord}")
    else:
        print("ERROR: Chord not identified")
        sys.exit(1)

if __name__ == "__main__":
    main()