from mood_analyser import MoodAnalysisException, MoodError


class MoodFactory:

    @staticmethod
    def create(class_name, *args):
        try:
            module = __import__("mood_analyser")
            cls = getattr(module, class_name)
            return cls(*args)
        except AttributeError:
            raise MoodAnalysisException(MoodError.NO_CLASS)
        except TypeError:
            raise MoodAnalysisException(MoodError.NO_METHOD)

    @staticmethod
    def invoke(obj, method_name):
        try:
            return getattr(obj, method_name)()
        except AttributeError:
            raise MoodAnalysisException(MoodError.NO_METHOD)

    @staticmethod
    def set_field(obj, field, value):
        if not hasattr(obj, field):
            raise MoodAnalysisException(MoodError.NO_FIELD)

        if value is None:
            raise MoodAnalysisException(MoodError.NULL)

        setattr(obj, field, value)
