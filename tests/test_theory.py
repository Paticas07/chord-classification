from classifier.theory import get_note, interval
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

