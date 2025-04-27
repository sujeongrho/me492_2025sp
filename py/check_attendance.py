import json
import os
print(os.getcwd())
with open('py/student_data.json', 'r',) as file:
    data = json.load(file)

for item in data:
    print(f"Name: {item['name']}, Major: {item['major']}, Role: {item['role']}")
    if item['name'] == 'Huitaek Yun':
        print("I love programming.")
