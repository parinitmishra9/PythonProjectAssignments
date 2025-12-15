# Exercise - Loops & dictionaries
# Delete the sensitive information from the dictionary present in a list
# sensitive information includes "password", "address"
users ={
        "username": "john_doe",
        "password": "12345",
        "email": "my_user@yahoo.com",
        "phone": "555-1234",
        "address": "123 Main St"
}
sensitive_info = ["password", "address"]
for info in sensitive_info:
    if info in users:
        del users[info]
print(users)
# Expected Output:
# {'username': 'john_doe', 'email': 'my_user@yahoo.com', 'phone': '555-1234'}
