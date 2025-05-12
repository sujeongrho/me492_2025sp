import json
import os
print(os.getcwd())
with open('./student_data.json', 'r',) as file:
    data = json.load(file)

''' --------------------------------------------'''
# Add your introduction
def htyun():
    print("I love programming.")
def hanbin_jang():
    print("I am the grader of this homework")
def jms5017():
    print("I am learning how to use github")
def hscotte978():
    print("I learned how to use Linux for the first time in this class.")
def moonsj4244():
    print("I think Git is interesting!")
def cvsdh01():
    print("Git is amazing !")
def abiezerjerom():
    print("This is my first time using Git")
def shtnwjd05():
    print("I'm sorry I'm late:(")
''' --------------------------------------------'''

for item in data:
    print(f"Name: {item['name']}, Major: {item['major']}, Role: {item['role']}")
    ''' --------------------------------------------'''
    ## Add your own function call
    if item['name'] == 'Huitaek Yun':
        htyun()   
    if item['name'] == 'Hanbin Jang':
        hanbin_jang()  
    if item['name'] == 'Minseo Jang':
        jms5017()
    if item['name'] == 'Jeongil Hwang':
        hscotte978()
    if item['name'] == 'Sunji Moon':
        moonsj4244()
    if item['name'] == 'Donghyeok Shin':
        cvsdh01()
    if item['name'] == 'Abiezer Jerom'
        abiezerjerom()
    if item['name'] == 'Sujeong Rho':
        shtnwjd05()
    ''' --------------------------------------------'''
