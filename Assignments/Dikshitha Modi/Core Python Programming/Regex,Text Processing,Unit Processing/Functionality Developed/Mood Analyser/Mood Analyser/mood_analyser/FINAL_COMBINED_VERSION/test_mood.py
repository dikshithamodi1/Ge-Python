import pytest
from mood_analyser import MoodAnalyser, MoodAnalysisException, MoodError
from factory import MoodFactory


# UC1
def test_sad():
    m = MoodAnalyser("I am sad")
    assert m.analyse_mood() == "SAD"


def test_happy():
    m = MoodAnalyser("I am happy")
    assert m.analyse_mood() == "HAPPY"


# UC2 + UC3
def test_null():
    with pytest.raises(MoodAnalysisException) as e:
        MoodAnalyser(None).analyse_mood()
    assert e.value.error == MoodError.NULL


def test_empty():
    with pytest.raises(MoodAnalysisException) as e:
        MoodAnalyser("").analyse_mood()
    assert e.value.error == MoodError.EMPTY


# UC4 reflection default
def test_reflection_default():
    obj = MoodFactory.create("MoodAnalyser")
    assert isinstance(obj, MoodAnalyser)


def test_wrong_class():
    with pytest.raises(MoodAnalysisException):
        MoodFactory.create("WrongClass")


# UC5 reflection parameter
def test_reflection_param():
    obj = MoodFactory.create("MoodAnalyser", "happy")
    assert obj.analyse_mood() == "HAPPY"


# UC6 invoke + set field
def test_invoke():
    obj = MoodAnalyser("sad")
    assert MoodFactory.invoke(obj, "analyse_mood") == "SAD"


def test_set_field():
    obj = MoodAnalyser()
    MoodFactory.set_field(obj, "message", "happy")
    assert obj.analyse_mood() == "HAPPY"


def test_wrong_field():
    obj = MoodAnalyser()
    with pytest.raises(MoodAnalysisException):
        MoodFactory.set_field(obj, "wrong", "happy")
