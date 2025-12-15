student1 = {"English", "Maths", "CS", "Chemistry", "Physics"}
student2 = {"English", "Biology", "Chemistry", "Physics"}
student3 = {"Sanskrit", "Maths", "CS"}

print(student1, type(student1))
print(student2, type(student2))

# Interaction: Common subjects opted by both students
common_subjects = student1.intersection(student2)
print("Common subjects:", common_subjects)
# Alternatively, we can use & operator
common_subjects = student1 & student2
print("Common subjects:", common_subjects)
# Empty set if no common subjects
common_subjects = student1.intersection(student2, student3)
print("Common subjects:", common_subjects)
# Alternatively, we can use & operator
common_subjects = student1 & student3
print("Common subjects:", common_subjects)

# Union: All subjects opted by both students
all_subjects = student1.union(student2, student3)
print("All subjects:", all_subjects)
# Alternatively, we can use | operator
all_subjects = student1 | student2 | student3
print("All subjects:", all_subjects)

# Difference: Subjects opted by student1 but not by student2
unique_subjects_student1 = student1.difference(student2)
print("Subjects unique to student1:", unique_subjects_student1)
# Alternatively, we can use - operator
unique_subjects_student1 = student1 - student2
print("Subjects unique to student1:", unique_subjects_student1)