# Chord Classifier CLI

A command-line Python tool that identifies and classifies musical triads.

The classifier analyzes a chord composed of three notes and determines:

The program accepts notes written using standard musical notation, including sharps ('#') and flats ('b').

## Features

- Classifies all basic triad chords
- Detects chord inversions automatically
- Supports accidentals (# and b)
- Provides clear CLI error messages

## Usage

Run the program from the project root:

```bash
python3 src/classifier/main.py NOTE1 NOTE2 NOTE3
```

The notes must:

- Be provided in ascending pitch order
- Use valid note names (A-G)
- Optionally include sharps (#) or flats (b)

Example:

```bash
 python3 src/classifier/main.py C E Ab
```

Output:

```text
Ab Augmented 1 inv
```

## Error Handling

The program validates user input and reports common errors.

- Invalid note name
    Error: NOTE is not a valid note.
    Please enter a valid pitch (A-G).

- Mixing sharps and flats
    Error: NOTE is not a valid note.
    Please use only # or b, do not use both.

- Invalid Accidentals
    Error: - is not a valid accident please use # or b.

- Too few arguments
    Error: You provided too little arguments.
    Please provide 3 notes

- Too many arguments
    Error: You provided too many arguments.
    Please provide 3 notes

- Invalid chord structure
    Error: Chord not identified

## Core Functionality

The tool accepts three musical notes as command-line arguments and analyzes their interval relationships to classify the chord.

For each input chord, the classifier determines:

- The root note
- The chord quality
    - Major
    - Minor
    - Diminished
    - Augmented
- The inversion state
    - Root position
    - 1st inversion
    - 2nd inversion

The program validates note formatting before processing and automatically attempts chord inversions when the initial note order does not form a valid triad structure.

The classifier supports accidentals using sharps (`#`) and flats (`b`) and rejects invalid note combinations or malformed pitch notation.

## Technical Implementation

1. **Input Parsing:**  
   Command-line arguments are parsed using Python's `argparse` module, including custom validation and error handling for incorrect argument counts.

2. **Note Representation:**  
   Musical notes are converted into internal note objects containing:
   - Base note value
   - Total semitone value
   - Accidental information

3. **Pitch Class Mapping:**  
   Notes are mapped into pitch classes (`0–11`) to simplify interval calculations and octave normalization.

4. **Interval Validation:**  
   The program validates whether adjacent notes form valid musical thirds before attempting classification.

5. **Automatic Inversion Detection:**  
   If the provided note order does not immediately produce a valid triad structure, the chord is automatically inverted until a valid interval structure is found.

6. **Chord Classification:**  
   The resulting interval pattern is matched against predefined triad interval combinations:
   - `4 + 3` → Major
   - `3 + 4` → Minor
   - `3 + 3` → Diminished
   - `4 + 4` → Augmented

7. **Output Generation:**  
   The final output displays:
   - Root note
   - Chord quality
   - Inversion state (when applicable)

## Project Status
- **Current Scope:** All triads with inversions.
- **Future Support:** 7th chords.

## Requirements
- Python 3.12.3