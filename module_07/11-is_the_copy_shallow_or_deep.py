# Copy Module
import copy

#  Understanding Shallow and Deep Copies in Python
#  what is Shallow Copy and Deep Copy
# Shallow Copy: A shallow copy creates a new object, but inserts references into it to the objects found in the original. Therefore, if the original object contains other objects (like lists or dictionaries), changes made to those nested objects in the copied object will also reflect in the original object.
# Example of Shallow Copy:
original_list = [1, 2, [3, 4], 5]
shallow_copied_list = copy.copy(original_list)
# modifying the top-level element in the shallow copied list
shallow_copied_list[0] = 10
# Modifying the nested list in the shallow copied list
shallow_copied_list[2][0] = 'Changed'
print(f"Original List before modification: {original_list}", id(original_list))
print(f"Shallow Copied List before modification: {shallow_copied_list}", id(shallow_copied_list))



# Deep Copy: A deep copy creates a new object and recursively adds copies of nested objects found in the original. This means that changes made to nested objects in the copied object will not affect the original object.
deep_copied_list = copy.deepcopy(original_list)
# modifying the top-level element in the deep copied list
deep_copied_list[1] = 20
# Modifying the nested list in the deep copied list
deep_copied_list[2][1] = 'DeepChanged'
print(f"Original List after deep copy modification: {original_list}", id(original_list))
print(f"Deep Copied List after modification: {deep_copied_list}", id(deep_copied_list))