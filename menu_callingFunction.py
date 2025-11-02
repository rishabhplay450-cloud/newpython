# ...existing code...
# Creating a tuple of tuples containing key-value pairs
student_data = (
    ('name', 'John'),
    ('age', 20),
    ('course', 'Python'),
    ('grade', 'A')
)

# ...existing code...
# Define a Student class and create an object from the tuple
class Student:
    def __init__(self, name=None, age=None, course=None, grade=None, data_tuple=None):
        if data_tuple:
            d = dict(data_tuple)
            self.name = d.get('name')
            self.age = d.get('age')
            self.course = d.get('course')
            self.grade = d.get('grade')
        else:
            self.name = name
            self.age = age
            self.course = course
            self.grade = grade

    def to_dict(self):
        return {'name': self.name, 'age': self.age, 'course': self.course, 'grade': self.grade}

    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age!r}, course={self.course!r}, grade={self.grade!r})"

# ...existing code...

# Menu-driven functions
def show_tuple():
    print("\nOriginal Tuple:", student_data)

def create_student_from_tuple():
    return Student(data_tuple=student_data)

def show_student():
    student = create_student_from_tuple()
    print("\nStudent object:", student)
    return student

def show_dict(student=None):
    if student is None:
        student = create_student_from_tuple()
    print("\nConverted Dictionary:", student.to_dict())

def update_tuple_from_input():
    global student_data
    print("\nEnter new values (press Enter to keep current value):")
    current = dict(student_data)
    name = input(f"Name [{current.get('name')}]: ").strip()
    age = input(f"Age [{current.get('age')}]: ").strip()
    course = input(f"Course [{current.get('course')}]: ").strip()
    grade = input(f"Grade [{current.get('grade')}]: ").strip()

    if name:
        current['name'] = name
    if age:
        try:
            current['age'] = int(age)
        except ValueError:
            current['age'] = age
    if course:
        current['course'] = course
    if grade:
        current['grade'] = grade

    student_data = tuple(current.items())
    print("\nUpdated tuple:", student_data)

def main_menu():
    student_obj = None
    while True:
        print("\nMenu:")
        print("1) Show original tuple")
        print("2) Create & show Student object from tuple")
        print("3) Show dictionary from Student object")
        print("4) Update tuple values")
        print("5) Exit")
        choice = input("Choose an option [1-5]: ").strip()

        if choice == '1':
            show_tuple()
        elif choice == '2':
            student_obj = show_student()
        elif choice == '3':
            show_dict(student_obj)
        elif choice == '4':
            update_tuple_from_input()
            student_obj = None
        elif choice == '5' or choice.lower() in ('q', 'exit'):
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main_menu()
# ...existing code...