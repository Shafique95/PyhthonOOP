

from oop.StudentDetails import StudentDetails
from oop.animal import Animal
from oop.dog import Dog


def main():
    print(f"starting point of app ")
    animal=Animal("Dog","red")
    animal.get_animal_name()
    animal.get_animal_color()
    animal.get_animal_info()
    dog=Dog("Caty dog","124536caty")
    dog.get_dog_details()
    student_details=StudentDetails(
        "Ashik",25,"Jaraitala High School"
    )
    student_details.get_student_details()

if __name__=="__main__":
    main()