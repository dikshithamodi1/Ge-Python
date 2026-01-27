class Student:
    def _init__(self,name):
        self.name=name
        self.attendance="Absent"
    def mark_present(self):
        self.attendance="Present"
    def mark_absent(self):
        self.attendance="Absent"
s=Student()
s.mark_present()
print(s.attendance)
