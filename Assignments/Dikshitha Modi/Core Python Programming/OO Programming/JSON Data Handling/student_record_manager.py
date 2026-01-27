import json
def save_student(students):
    with open("students.json","w") as file:
        json.dump(students,file)
def load_students():
    with open("students.json","r") as file:
        return json.load(file)
students = [
{"name": "Riya", "grade": "A", "age": 20},
{"name": "John", "grade": "B", "age": 21}
]
save_student(students)
print(load_students())
        
