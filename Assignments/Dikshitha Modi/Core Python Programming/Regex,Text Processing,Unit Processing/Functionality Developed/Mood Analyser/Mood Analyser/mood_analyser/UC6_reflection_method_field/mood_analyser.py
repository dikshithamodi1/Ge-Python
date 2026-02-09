class MoodAnalyser:

    def __init__(self):
        self.message = None

    def analyse_mood(self):
        if "sad" in self.message.lower():
            return "SAD"
        return "HAPPY"
