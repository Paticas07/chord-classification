from classifier.theory import get_note
def test_note_mapping():
    # Test natural notes
    assert get_note("C").total_value == 0
    assert get_note("B").total_value == 11
    
    # Test enharmonics (Sharps and Flats)
    assert get_note("C#").total_value == 1
    assert get_note("Db").total_value == 1
    
    # Test wrap-around
    assert get_note("B#").total_value == 0
    assert get_note("Cb").total_value == 11
    
    # Test double accidentals (just in case!)
    assert get_note("C##").to == 2

if __name__ == "__main__":
    test_note_mapping()
    print("All tests passed!")