class MoodFactory:

    @staticmethod
    def invoke(obj, method):
        return getattr(obj, method)()

    @staticmethod
    def set_field(obj, field, value):
        setattr(obj, field, value)
