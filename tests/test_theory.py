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
    
    def double_accidentals(self):
        assert get_note("C##").total_value == 2

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
        # Verify the first note's pitch class is 0 (C)
        assert result.root.total_value == 0 

    def test_invalid_input(self):
        # Testing what happens with 2 notes if your function handles it
        result = parse_args(["C", "E"]) 
        assert result is None

    def test_cli_output(self, capsys, monkeypatch):
    # This simulates typing: python main.py C E G
        monkeypatch.setattr(sys, 'argv', ['main.py', 'C', 'E', 'G'])

        main()

        # Capture what was printed to the terminal
        captured = capsys.readouterr()
        assert "Chord identified" in captured.out
