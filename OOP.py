'''
Attributes are datatypes and methods are function in class
class is blueprint
object is instance of class
The type() function determines the class (or type) of a variable or value.
By using type(" "), we can determine that the class of the given value is a string.
Strings have various methods associated with them.
The upper() method is one such method that returns the string in all uppercase.
Another method is isnumeric(), which returns a boolean indicating whether the string is a number or not.
The dir() function can be used to print all the attributes and methods of an object.
Each string is an instance of the string class and inherits the same methods from its parent class.
The methods of a string can return different values based on the content of the string.
The help() function can be used on an object to obtain the documentation for its corresponding class.
The documentation provides information about the class's methods, including their parameters, return value types, and descriptions.

'''
"""
Syntax:
Class Classname: => in py classname is alway starts with capital letter
Eg 
Class Apple:
 color: ""
 flavour: ""
 
 ram=Apple()
 ram.color="red"
 ram.flavour="sweet"
 print(ram.color)  => Output: red
 print(ram.flavour.upper())  => Output: SWEET

golden = Apple()
golden.color = "Yellow"
golden.flavor = "Soft"
"""
"""
1. Calling methods on objects executes functions that operate on attributes of a specific instance of the class.
2. Methods modify the state or behavior of the specific instance they are called on, rather than affecting all instances of the class globally.
3. Methods are defined within a class by creating functions inside the class definition.
4. Instance methods in a class can take a parameter called `self`, which represents the instance the method is being executed on.
5. The `self` parameter allows accessing attributes of the instance using dot notation, such as `self.name`, to access the `name` attribute of that specific instance.
6. Variables that contain different values for different instances are known as instance variables.
7. Instance variables hold unique data for each instance of the class, allowing each instance to have its own state.
8. By using instance variables, different objects of the same class can store and manipulate data independently without affecting each other.
"""
"""
class Apple:
def init(self, color, flavor):
self.color = color
self.flavor = flavor

jonagold = Apple("red", "sweet")
print(jonagold.color)

 >>> class Apple:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor
...     def __str__(self):
...         return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

>>> jonagold = Apple("red", "sweet")
>>> print(jonagold)
This apple is red and its flavor is sweet

 
