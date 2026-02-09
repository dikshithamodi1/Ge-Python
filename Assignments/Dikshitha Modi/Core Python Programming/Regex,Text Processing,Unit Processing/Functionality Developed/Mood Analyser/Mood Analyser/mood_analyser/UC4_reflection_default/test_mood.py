from factory import MoodFactory
from mood_analyser import MoodAnalyser
import pytest

def test_create():
    obj = MoodFactory.create("MoodAnalyser")
    assert isinstance(obj, MoodAnalyser)

def test_wrong_class():
    with pytest.raises(Exception):
        MoodFactory.create("Wrong")
