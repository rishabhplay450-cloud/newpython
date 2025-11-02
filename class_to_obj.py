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

# Create Student object from the tuple
student = Student(data_tuple=student_data)

# Print outputs
print("Original Tuple:", student_data)
print("Student object:", student)
print("Converted Dictionary:", student.to_dict())
# ...existing code...