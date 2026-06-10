#classes and Objects
"""
objects => a container
    => data-> attributes
    => functionality -> methods/behaviour

"""

fruits = ["mango", "apple", "orange"]
print(type(fruits))
#fruits is an object of a class
fruits.append("grapes")

"""'
car1 
     => brand = "BMW", model="XYZ3",, year = 2023
     => accelerate, brake 

dot notations (.)

car1.brand => "BMW"
car1.accelerate(10)
"""

#Creating objects => we need classes

#Classes => template/blueprints/design used for creating objects
#Also called as type

#Objects are created using the class
#Instances of a class

#Creating a class

class MyClass:
    pass


#Creating an object
obj1 = MyClass()
obj2 = MyClass()

#obj1 and obj2 are objects of class MyClass

l1 = [10,20,30]
print(type(l1)) #o/p => <class 'list'>

print(type(obj1)) #o/p =>  <class '__main__.MyClass'>
print(type(obj2)) #o/p =>  <class '__main__.MyClass'>

#Calling Methods using objects?
# obj1.method(arg1, arg2, ...)

class Student:
    """
    This is a class Student to manage student information and activities 
    """
    pass

s1 = Student()
s2 = Student()

#Doc strings => __doc__
print(Student.__doc__)
#o/p => This is a class Student to manage student information and activities
print(help(Student))
#o/p => everything related to class Student
