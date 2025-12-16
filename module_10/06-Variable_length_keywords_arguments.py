# Variable length keywords arguments:
# are used when you want to pass a variable number of keyword arguments to a function.
# In Python, this is done using the **kwargs syntax (0 to n).
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York

def student_details(sid, sname, *extra, **marks):
    if len(marks) == 0:
        print(f"Student ID: {sid}, Name: {sname}, did not attend the exam.")
    else:
        percent = sum(marks.values()) / len(marks) if marks else 0
        print(f"Student ID: {sid}, Name: {sname}, Percentage: {round(percent, 2)}%")
    print(f"{sname} does extra curricular activities: {', '.join(extra) if extra else 'None'}")
student_details(101, "Bob",  "Football", "Cricket", Math=85, Science=90, English=78)
# Output: Student ID: 101, Name: Bob, Percentage: 84.33
student_details(102, "Charlie", "Basketball")
# Output: Student ID: 102, Name: Charlie, did not attend the exam.