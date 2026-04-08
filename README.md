# Chord Classifier CLI

A Python-based utility to identify musical triads from three-note inputs.

## Core Functionality
The tool accepts three musical notes as command-line arguments and returns the corresponding chord classification (e.g., Major, Minor, Diminished, or Augmented).

## Technical Implementation
1.  **Note Mapping:** Converts note names (handling enharmonics like C# and Db) into pitch class integers (0–11).
2.  **Interval Analysis:** Calculates the semitone distance between notes to determine the chord structure.
3.  **Pattern Matching:** Identifies the triad type based on internal interval definitions.

## Project Status
- **Current Scope:** Root-position triads only.
- **Future Support:** Inversions and 7th chords.

## Requirements
- Python 3.12.3