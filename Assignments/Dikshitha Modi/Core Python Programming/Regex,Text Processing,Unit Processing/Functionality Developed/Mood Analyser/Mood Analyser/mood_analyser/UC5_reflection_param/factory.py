class MoodFactory:

    @staticmethod
    def create(class_name, msg):
        module = __import__("mood_analyser")
        cls = getattr(module, class_name)
        return cls(msg)
