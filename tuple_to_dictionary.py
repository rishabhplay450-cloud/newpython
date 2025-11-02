# Creating a tuple of tuples containing key-value pairs
student_data = (
    ('name', 'John'),
    ('age', 20),
    ('course', 'Python'),
    ('grade', 'A')
)

# Converting tuple to dictionary using dict() constructor
student_dict = dict(student_data)

# Printing the original tuple
print("Original Tuple:", student_data)

# Printing the converted dictionary
print("Converted Dictionary:", student_dict)