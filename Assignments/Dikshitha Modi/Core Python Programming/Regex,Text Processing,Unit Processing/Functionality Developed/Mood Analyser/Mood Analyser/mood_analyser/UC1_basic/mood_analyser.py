class MoodAnalyser:

    def analyse_mood(self, message):
        if "sad" in message.lower():
            return "SAD"
        return "HAPPY"
