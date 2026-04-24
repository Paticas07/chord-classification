from classifier.theory import *
from classifier.main import *
from classifier.models import *
import pytest

class TestNoteMapping():
    # Issue #2
    def test_natural_notes(self):
        assert get_note("C").total_value == 0
        assert get_note("B").total_value == 11
    
    def test_enharmonics(self):
        assert get_note("C#").total_value == 1
        assert get_note("Db").total_value == 1
    
    def test_wrap_around(self):
        assert get_note("B#").total_value == 0
        assert get_note("Cb").total_value == 11
    
    def test_double_accidentals(self):
        assert get_note("C##").total_value == 2
    
    def test_accidental_storage(self):
        c_sharp = get_note("C#")
        assert c_sharp.acc == "#"
    
        d_flat = get_note("Db")
        assert d_flat.acc == "b"

        c_double_sharp = get_note("C##")
        assert c_double_sharp.acc == "##"

class TestNoteDistance:
    def test_simple_intervals(self):
        c = get_note("C")
        e = get_note("E")
        g = get_note("G")
        assert interval(c,e) == 4
        assert interval(e,g) == 3
    def test_wrap_around_dist(self):
        b = get_note("B")
        d = get_note ("D")
        assert interval (b,d) == 3

class TestParseArgs:
    def test_valid_triad_conversion(self):
        result = parse_args(["C", "E", "G"])
        assert result is not None
        assert result.root.total_value == 0 

    def test_invalid_input(self):
        result = parse_args(["C", "E"]) 
        assert result is None

    def test_cli_output(self, capsys, monkeypatch):
        monkeypatch.setattr(sys, 'argv', ['main.py', 'C', 'E', 'G'])

        main()

        # Capture what was printed to the terminal
        captured = capsys.readouterr()
        assert "C Major" in captured.out
        
class TestInputValidation:
    """Tests all aspects of user input, from note strings to CLI arguments."""
    
    def test_valid_note_parsing(self):
        """Checks if standard notes are converted to Note objects correctly."""
        note = get_note("C#")
        assert note.total_value == 1
        assert note.base == 0

    def test_invalid_pitch_letter(self):
        """Ensures that a non A-G letter triggers a SystemExit."""
        with pytest.raises(SystemExit) as e:
            get_note("X")
        assert e.value.code == 1

    def test_contradictory_accidentals(self):
        """Ensures that mixing # and b (e.g., C#b) is rejected."""
        with pytest.raises(SystemExit) as e:
            get_note("C#b")
        assert e.value.code == 1

    # --- CLI Argument Validation ---

    def test_too_few_arguments(self, capsys, monkeypatch):
        """Checks if providing only 2 notes triggers our custom error message."""
        monkeypatch.setattr(sys, 'argv', ['main.py', 'C', 'E'])
        
        with pytest.raises(SystemExit) as e:
            main()
        
        captured = capsys.readouterr()
        assert "too little arguments" in captured.out
        assert e.value.code == 2

    def test_too_many_arguments(self, capsys, monkeypatch):
        """Checks if providing 4 notes triggers our custom error message."""
        monkeypatch.setattr(sys, 'argv', ['main.py', 'C', 'E', 'G', 'B'])
        
        with pytest.raises(SystemExit) as e:
            main()
        
        captured = capsys.readouterr()
        assert "too many arguments" in captured.out
        assert e.value.code == 2

class TestChordIntervals:
    """Verifies that interval_chord returns the correct interval tuples."""

    def test_major_signature(self):
        c = Chord(Note(0, 0,''), Note(4, 4,''), Note(7, 7,''))
        assert interval_chord(c) == (4, 3)

    def test_minor_signature(self):
        c = Chord(Note(2, 2,''), Note(5, 5,''), Note(9, 9,''))
        assert interval_chord(c) == (3, 4)

class TestChordIdentification:
    """Verifies that the classifier correctly identifies chord names."""

    def test_major_chord_identification(self, capsys, monkeypatch):
        monkeypatch.setattr(sys, 'argv', ['main.py', 'C', 'E', 'G'])
        main()
        captured = capsys.readouterr()
        assert "C Major" in captured.out

    def test_minor_chord_identification(self, capsys, monkeypatch):
        monkeypatch.setattr(sys, 'argv', ['main.py', 'C', 'Eb', 'G'])
        main()
        captured = capsys.readouterr()
        assert "C Minor" in captured.out
        
    def test_sharp_major_identification(self, capsys, monkeypatch):
        monkeypatch.setattr(sys, 'argv', ['main.py', 'C#', 'E#', 'G#'])
        main()
        captured = capsys.readouterr()
        assert "C# Major" in captured.out

    def test_unknown_chord_failure(self, capsys, monkeypatch):
        monkeypatch.setattr(sys, 'argv', ['main.py', 'C', 'F', 'G'])
        with pytest.raises(SystemExit) as e:
            main()
        captured = capsys.readouterr()
        assert "Error: interval formed" in captured.out
        assert e.value.code == 1
    
class TestUnit:
    """Verifys all types of chords"""
    def test_chord1(self,capsys, monkeypatch):
        monkeypatch.setattr(sys,'argv', ['main.py', 'C', 'E', 'G&'])
        with pytest.raises(SystemExit) as e:
            main()
        captured = capsys.readouterr()
        assert "not a valid accident" in captured.out
        assert e.value.code == 1

    def test_chord2(self,capsys, monkeypatch):
        monkeypatch.setattr(sys,'argv', ['main.py', 'D', 'F', 'H'])
        with pytest.raises(SystemExit) as e:
            main()
        captured = capsys.readouterr()
        assert "not a valid note" in captured.out
        assert e.value.code == 1 

    def test_chord3(self,capsys, monkeypatch):
        monkeypatch.setattr(sys,'argv', ['main.py', 'c', 'E', 'g'])
        main()
        captured = capsys.readouterr()
        assert "C Major" in captured.out
    
    def test_chord4(self,capsys, monkeypatch):
        monkeypatch.setattr(sys,'argv', ['main.py', 'C', 'E', 'Ab'])
        with pytest.raises(SystemExit) as e:
            main()
        captured = capsys.readouterr()
        assert "Error: interval" in captured.out
        assert e.value.code == 1
    
    def test_chord5(self,capsys, monkeypatch):
        monkeypatch.setattr(sys,'argv', ['main.py', 'G', 'B', 'D'])
        main()
        captured = capsys.readouterr()
        assert "G Major" in captured.out

    def test_chord6(self, capsys, monkeypatch):
        monkeypatch.setattr(sys, 'argv', ['main.py', 'F##', 'A##', 'C###'])
        main()
        captured = capsys.readouterr()
        assert "Augmented" in captured.out
    



