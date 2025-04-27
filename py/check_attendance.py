import json
import os
print(os.getcwd())
with open('py/student_data.json', 'r',) as file:
    data = json.load(file)

''' --------------------------------------------'''
# Add your introduction
def htyun():
    print("I love programming.")
def hanbin_jang():
    print("I am the grader of this homework")
''' --------------------------------------------'''

for item in data:
    print(f"Name: {item['name']}, Major: {item['major']}, Role: {item['role']}")
    ''' --------------------------------------------'''
    ## Add your own function call
    if item['name'] == 'Huitaek Yun':
        htyun()   
    if item['name'] == 'Hanbin Jang':
        hanbin_jang()  
    ''' --------------------------------------------'''
