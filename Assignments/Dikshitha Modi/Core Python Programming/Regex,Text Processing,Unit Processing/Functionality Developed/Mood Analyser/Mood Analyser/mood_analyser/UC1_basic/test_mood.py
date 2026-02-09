from mood_analyser import MoodAnalyser

def test_sad():
    m = MoodAnalyser()
    assert m.analyse_mood("I am in Sad Mood") == "SAD"

def test_happy():
    m = MoodAnalyser()
    assert m.analyse_mood("I am in Any Mood") == "HAPPY"
