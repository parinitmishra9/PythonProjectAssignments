# The pickle module is used for serializing and deserializing Python object structures.
import pickle
# byte stream: A sequence of bytes that can represent any type of data.
# Serialization is the process of converting a Python object into a byte stream,
# while deserialization is the process of converting a byte stream back into a Python object.
# Example of serialization
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Serialize the data to a byte stream
serialized_data = pickle.dumps(data)
print("Serialized Data:", serialized_data)
# Example of deserialization
# Deserialize the byte stream back to a Python object
deserialized_data = pickle.loads(serialized_data)
print("Deserialized Data:", deserialized_data)
# You can also serialize and deserialize objects to and from files using pickle.dump() and pickle.load().
# Serialize to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
# Deserialize from a file
with open('data.pkl', 'rb') as file:
    file_data = pickle.load(file)
print("File Deserialized Data:", file_data)
# Note: Be cautious when unpickling data from untrusted sources, as it can lead to security vulnerabilities.