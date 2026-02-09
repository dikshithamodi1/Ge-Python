from mood_analyser import MoodAnalyser

def test_null():
    m = MoodAnalyser(None)
    assert m.analyse_mood() == "HAPPY"
