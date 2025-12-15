# Fetch the marks of a student and update it
student_alice = {
    "Maths": 85,
    "English": 90,
    "Physics": 78
}

# Fetching marks in English
english_marks = student_alice["English"]
print(f"Alice's marks in English: {english_marks}")
# get() method to fetch value
physics_marks = student_alice.get("Physics")
print(f"Alice's marks in Physics: {physics_marks}")
# Updating marks in Maths
student_alice["Maths"] = 88
print("Updated Alice's marks in Maths:", student_alice)
#  get returns None if key not found
history_marks = student_alice.get("History")
print(f"Alice's marks in History: {history_marks}")
# Using get with default value
history_marks_default = student_alice.get("History", 0)
print(f"Alice's marks in History (with default): {history_marks_default}")
# Deleting an entry using del
del student_alice["Physics"]
print("After deleting Physics marks:", student_alice)
# Deleting an entry using pop()
english_marks_deleted = student_alice.pop("English")
print(f"Deleted English marks: {english_marks_deleted}")
print("After deleting English marks:", student_alice)
# Using popitem() to remove the last inserted item
last_item = student_alice.popitem()
print(f"Removed last item: {last_item}")
print("After popitem:", student_alice)
# Trying to delete a non-existing key using pop() with default value
science_marks_deleted = student_alice.pop("Science", "Not Found")
print(f"Attempted to delete Science marks: {science_marks_deleted}")
print("Final state of Alice's marks:", student_alice)

# Membership operators
is_maths_present = "Maths" in student_alice
print(f"Is Maths present in Alice's subjects? {is_maths_present}")
is_physics_present = "Physics" in student_alice
print(f"Is Physics present in Alice's subjects? {is_physics_present}")

# Updating dictionary with another dictionary
student_alice = {
    "Maths": 85,
    "English": 90,
    "Physics": 78
}

additional_marks = {
    "Chemistry": 92,
    "Biology": 88
}
student_alice.update(additional_marks)
print("After updating with additional marks:", student_alice)

# if a key exists in both dictionaries, the value from the second dictionary overwrites the first
student_alice_sem1 = {
    "Maths": 85,
    "English": 90,
    "Physics": 78
}

student_alice_sem2 = {
    "Maths": 92,
    "Biology": 88
}
student_alice_sem1.update(student_alice_sem2)
print("After updating with semester 2 marks:", student_alice_sem1)

# if 2 keys are same in both dictionaries, the value from the second dictionary overwrites the first
# python reads the dictionary from left to right
# keys must be unique in a dictionary, cannot have duplicate keys
student_bob = {
    "History": 75,
    "Geography": 80,
    "History": 82,
    "Civics": 78
}
print("After updating Bob's marks:", student_bob)