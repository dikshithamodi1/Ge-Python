from mood_analyser import MoodAnalysisException

class MoodFactory:

    @staticmethod
    def create(class_name):
        try:
            module = __import__("mood_analyser")
            cls = getattr(module, class_name)
            return cls()
        except:
            raise MoodAnalysisException("NO_CLASS")
