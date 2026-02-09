from enum import Enum


class MoodError(Enum):
    NULL = 1
    EMPTY = 2
    NO_CLASS = 3
    NO_METHOD = 4
    NO_FIELD = 5


class MoodAnalysisException(Exception):
    def __init__(self, error):
        self.error = error
        super().__init__(str(error))


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

    def __eq__(self, other):
        return isinstance(other, MoodAnalyser)
