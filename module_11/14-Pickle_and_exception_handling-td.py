# Pickle and exception handling in Python
import pickle

students = {
    'student1': {'roll': 101, 'name': 'John',  'percent': 78.5},
    'student2': {'roll': 102, 'name': 'Carol', 'percent': 92.5},
    'student3': {'roll': 103, 'name': 'Alice', 'percent': 81.5},
}

print(students)
print(type(students))

# 1) Serialize the whole object to `students.bin`
with open('students.bin', 'wb') as fh:
    for student in students:
        pickle.dump(students[student], fh)

print("Serialized full students dict to `students.bin`")

# 2) Deserialize with exception handling
try:
    with open('students.bin', 'rb') as fh:
        loaded_students = pickle.load(fh)
except FileNotFoundError:
    print("File not found: `students.bin`")
except pickle.UnpicklingError:
    print("Data in `students.bin` is not a valid pickle")
except Exception as e:
    print("Unexpected error while loading:", type(e).__name__, e)
else:
    print("Loaded students (whole):", loaded_students)

# 3) Write multiple objects to the same file (one pickle per student)
with open('students_multi.bin', 'wb') as fh:
    for s in students.values():
        pickle.dump(s, fh)
print("Serialized individual student dicts to `students_multi.bin`")

# 4) Read multiple objects until EOFError
print("Deserializing from `students_multi.bin`:")
try:
    with open('students_multi.bin', 'rb') as fh:
        while True:
            try:
                obj = pickle.load(fh)
            except EOFError:
                break
            print("  ->", obj)
except FileNotFoundError:
    print("File not found: `students_multi.bin`")

# 5) Custom exception and validation with try/except/finally
class InvalidPercentageError(Exception):
    """Raised when a student's percentage is outside 0-100."""
    pass

def validate_student(s):
    p = s.get('percent')
    if p is None or not (0 <= p <= 100):
        raise InvalidPercentageError(f"Invalid percent {p} for {s.get('name')}")
    return True

# Demonstrate validation
for student in students.values():
    try:
        validate_student(student)
    except InvalidPercentageError as e:
        print("Validation error:", e)
    else:
        print(f"Student {student['name']} passed validation.")
    finally:
        print(f"Finished validation for {student['name']}\n")
        print("Finished validation for", s.get('name'))



