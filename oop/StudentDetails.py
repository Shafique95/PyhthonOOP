class StudentDetails:
    def __init__(self,name, age,school):
        self.name=name
        self.age=age
        self.school=school
    def get_student_details(self):
        print(f"The details of student is name: {self.name} age:{self.age} school:{self.school}")