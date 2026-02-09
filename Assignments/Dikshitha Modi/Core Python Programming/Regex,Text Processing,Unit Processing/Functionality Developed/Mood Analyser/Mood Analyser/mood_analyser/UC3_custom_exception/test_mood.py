import pytest
from mood_analyser import MoodAnalyser, MoodAnalysisException

def test_null():
    with pytest.raises(MoodAnalysisException):
        MoodAnalyser(None).analyse_mood()

def test_empty():
    with pytest.raises(MoodAnalysisException):
        MoodAnalyser("").analyse_mood()
