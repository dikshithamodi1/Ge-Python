from enum import Enum

class MoodError(Enum):
    NULL = 1
    EMPTY = 2

class MoodAnalysisException(Exception):
    def __init__(self, error):
        self.error = error

class MoodAnalyser:

    def __init__(self, message=None):
        self.message = message

    def analyse_mood(self):

        if self.message is None:
            raise MoodAnalysisException(MoodError.NULL)

        if self.message == "":
            raise MoodAnalysisException(MoodError.EMPTY)

        if "sad" in self.message.lower():
            return "SAD"

        return "HAPPY"
