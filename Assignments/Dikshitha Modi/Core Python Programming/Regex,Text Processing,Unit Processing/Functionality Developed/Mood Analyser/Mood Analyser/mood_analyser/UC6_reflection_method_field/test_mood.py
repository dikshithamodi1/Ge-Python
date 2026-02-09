from mood_analyser import MoodAnalyser
from factory import MoodFactory

def test_set_field():
    m = MoodAnalyser()
    MoodFactory.set_field(m, "message", "happy")
    assert MoodFactory.invoke(m, "analyse_mood") == "HAPPY"
