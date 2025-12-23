# The json module in Python provides functions for working with JSON (JavaScript Object Notation) data.
# JSON is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate.
# The json module allows you to convert Python objects to JSON format and vice versa.
import json
from plistlib import dumps

# Example of converting a Python dictionary to a JSON string
python_dict = {"name": "Alice", "age": 30, "city": "New York"}
json_string = json.dumps(python_dict)
print("JSON String:", json_string)

students = {
    "student_1": {
    "name": "John",
    "age": 21,
    "courses": ["Math", "CompSci"],
        "sports": True
    },
    "student_2": {
    "name": "Jane",
    "age": 22,
    "courses": ["History", "Art"],
    "sports": False
    },
    "student_3": {
    "name": "Dave",
    "age": 20,
    "courses": ["Biology", "Chemistry"],
    "sports": True
    }
}

print(f"Students Dictionary: {students}")
print(f"Type of students: {type(students)}")

# dump() -> Write JSON data to a file
with open("students.json", "w") as file:
    json.dump(students, file)

# dump() -> with indentation for better readability
with open("students_pretty.json", "w") as file:
    json.dump(students, file, indent=4)

# load() -> Read JSON data from a file
with open("students.json", "r") as file:
    students_from_file = json.load(file)
print(f"Students from file: {students_from_file}")
print(f"Type of students_from_file: {type(students_from_file)}")

# update() -> Modifying the loaded data
students_from_file["student_1"]["age"] = 22
print(f"Updated Students from file: {students_from_file}")
print(f"Type of updated students_from_file: {type(students_from_file)}")

# dumps() -> Convert Python object to JSON string
students_json = json.dumps(students)
print(f"Students JSON String: {students_json}")
print(f"Type of students_json: {type(students_json)}")

# dumps() -> with indentation for better readability
students_json_pretty = json.dumps(students, indent=4)
print(f"Students JSON Pretty String: {students_json_pretty}")
print(f"Type of students_json_pretty: {type(students_json_pretty)}")

# Example of converting a JSON string back to a Python dictionary
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
python_dict = json.loads(json_string)
print("Python Dictionary:", python_dict)

# Example of working with a list of dictionaries
json_string = '''[
    {"name": "Bob", "age": 25, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "Los Angeles"}
]'''
python_list = json.loads(json_string)
print("Python List of Dictionaries:", python_list)
for person in python_list:
    print(f"{person['name']} is {person['age']} years old and lives in {person['city']}.")
# Example of nested JSON data and accessing its elements
json_string = '''{
    "company": "TechCorp",
    "employees": [
        {"name": "David", "position": "Developer"},
        {"name": "Eva", "position": "Designer"}
    ],
    "location": {"city": "Seattle", "state": "WA"}
}'''
python_data = json.loads(json_string)
print("Company:", python_data["company"])
print("Employees:")
for employee in python_data["employees"]:
    print(f" - {employee['name']}, {employee['position']}")
print("Location:", python_data["location"]["city"], ",", python_data["location"]["state"])
# Example of handling JSON data with special characters
json_string = '{"message": "Hello, \\nWorld! \\"Special\\" characters: \\t tab, \\u2602 umbrella."}'
python_data = json.loads(json_string)
print("Message:", python_data["message"])
# Example of pretty-printing JSON data
python_dict = {
    "fruits": ["apple", "banana", "cherry"],
    "vegetables": ["carrot", "broccoli", "spinach"]
}
json_string = json.dumps(python_dict, indent=4)
print("Pretty-printed JSON String:\n", json_string)
# Example of using custom separators in JSON serialization
python_dict = {"name": "Frank", "age": 28, "city": "Chicago"}
json_string = json.dumps(python_dict, separators=(", ", " = "))
print("Custom Separator JSON String:", json_string)
# Example of sorting keys in JSON serialization
python_dict = {"b": 2, "a": 1, "c": 3}
json_string = json.dumps(python_dict, sort_keys=True)
print("Sorted Keys JSON String:", json_string)
# Example of encoding and decoding JSON data with UTF-8
python_dict = {"greeting": "Hello, 世界"}
json_string = json.dumps(python_dict, ensure_ascii=False)
print("UTF-8 JSON String:", json_string)
decoded_dict = json.loads(json_string)
print("Decoded Dictionary:", decoded_dict)
# Example of handling JSONDecodeError exception
invalid_json_string = '{"name": "George", "age": 29, "city": "Boston"'
try:
    python_data = json.loads(invalid_json_string)
except json.JSONDecodeError as e:
    print("JSONDecodeError:", e)
# Example of using JSON with custom objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def person_to_dict(person):
    return {"name": person.name, "age": person.age}
person = Person("Hannah", 26)
json_string = json.dumps(person, default=person_to_dict)
print("Custom Object JSON String:", json_string)
decoded_dict = json.loads(json_string)
print("Decoded Dictionary from Custom Object:", decoded_dict)
# Example of using object_hook to decode JSON into custom objects
def dict_to_person(dct):
    return Person(dct["name"], dct["age"])
json_string = '{"name": "Ian", "age": 31}'
person = json.loads(json_string, object_hook=dict_to_person)
print("Decoded Person Object:", person.name, person.age)
# Example of working with JSON arrays
json_string = '[{"item": "book", "price": 12.99}, {"item": "pen", "price": 1.99}]'
python_list = json.loads(json_string)
print("JSON Array as Python List:", python_list)
for item in python_list:
    print(f"Item: {item['item']}, Price: {item['price']}")
# Example of nested JSON arrays and objects
json_string = '''{
    "store": {
        "name": "Bookstore",
        "books": [
            {"title": "1984", "author": "George Orwell"},
            {"title": "To Kill a Mockingbird", "author": "Harper Lee"}
        ]
    }
}'''
python_data = json.loads(json_string)
print("Store Name:", python_data["store"]["name"])
print("Books:")
for book in python_data["store"]["books"]:
    print(f" - {book['title']} by {book['author']}")
# Example of using JSON with boolean and null values
json_string = '{"isActive": true, "isVerified": false, "middleName": null}'
python_data = json.loads(json_string)
print("Boolean and Null Values:", python_data)
print("isActive:", python_data["isActive"])
print("isVerified:", python_data["isVerified"])
print("middleName:", python_data["middleName"])
# Example of converting a Python list to a JSON array string
python_list = ["red", "green", "blue"]
json_array_string = json.dumps(python_list)
print("JSON Array String:", json_array_string)
# Example of converting a JSON array string back to a Python list
json_array_string = '["circle", "square", "triangle"]'
python_list = json.loads(json_array_string)
print("Python List from JSON Array String:", python_list)