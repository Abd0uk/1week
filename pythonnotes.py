# comments => python interpreter will ignore it and will not excute it
# print("hello world") - this will not be printed because it starts with # sign


# Built-in functions in python
print() # function that used to show output in the CLI (Command Line Interface)

# Arguments => value that sent to the function 
print("Hello Sarah") # in that case the argument was "Hello Sarah"


# Variables = is like a box holds a value that can be changed 
name = "Sarah"
city = "Cairo"

print("my name is", name, "i'am from", city)

# Note: the flow of execution is always top to bottom / left to right
# so i can't use a variable as an argument in a function before i define it first

# Summary of what we discussed
# CLI vs GUI
# Functions intro
# Argument intro
# variables intro
# Flow of Excution => top to bottom / left to right


first_name="Sarah"
second_name="Afifi"
city="Cairo"

print("my name is", first_name, second_name, "I am from", city)

greetings="Good Night"
print(greetings)

name = 'Sarah'

txt =  "  'i'm " 


# string  = text 

# numbers 
# integer (int)
#  phone numner
# float 2.4 prices 

# year = 2003
# age = 2024 - year 
# print(age)


# variable = value
# value = string, integer , float and more and more and argument

# print()


# built in funcitons - provided by python 


# user defined funditon 

def show_age(birth_year):
    current_year = 2024
    age = current_year - birth_year
    print(age)


show_age(2004)