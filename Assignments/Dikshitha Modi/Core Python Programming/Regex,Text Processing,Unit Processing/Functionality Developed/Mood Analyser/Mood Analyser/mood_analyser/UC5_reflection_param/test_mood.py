from factory import MoodFactory
from mood_analyser import MoodAnalyser

def test_param_constructor():
    obj = MoodFactory.create("MoodAnalyser", "Happy")
    assert isinstance(obj, MoodAnalyser)
