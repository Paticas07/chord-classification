from classifier.theory import *
from classifier.models import *
import argparse
import sys

class ChordParser(argparse.ArgumentParser):
    def error(self, message):
        # Check if the error is about the number of arguments
        if "the following arguments are required" in message:
            print("Error: You provided too little arguments.\nPlease provide 3 notes")
        elif "unrecognized arguments" in message:
            # This triggers if more than 3 are provided
            print("Error: You provided too many arguments.\nPlease provide 3 notes")
        else:
            print(f"Error: {message}")
        
        self.print_help()
        sys.exit(2)

def parse_args (input:list) -> Chord:
    notes = [get_note(n) for n in input]
    if len(notes) == 3:
        return Chord(*notes)
    else:
        return None

def find_chord(chord:tuple) -> str:
    if chord not in CHORDS:
        print("Error: Chord not identified")
        sys.exit(1)
    else:
        return CHORDS[chord]
    
def main ():
    parser = ChordParser(description="Chord Classifier")

    parser.add_argument("notes", nargs=3, help= "Notes of the chord in ascending pitch")
    raw_chord = parser.parse_args()
    chord = parse_args(raw_chord.notes)

    if chord:
        t_chord = find_chord(interval_chord(chord))
        print(f"Chord identified: {t_chord}")
    else:
        print("Error: Chord not identified")
        sys.exit(1)

if __name__ == "__main__":
    main()