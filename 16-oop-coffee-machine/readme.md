Object-Oriented Programming (OOP) is a programming paradigm that is based on the concept of objects, which can contain data and code to manipulate that data. Python is an object-oriented programming language, which means that it supports the creation of objects and classes.

In Python, a class is a blueprint for creating objects. It defines the properties and methods that an object of that class will have. To create an object of a class, you use the __init__() method, which is called when the object is created. This method initializes the object's properties and sets their initial values.

Here is an example of a simple class in Python:
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")
```

In this example, we define a Person class that has two properties (name and age) and one method (say_hello). The __init__() method initializes the name and age properties when a new Person object is created. The say_hello() method prints a message that includes the person's name and age.

To create a new Person object, you can use the following code:
```py
person = Person("John", 30)
```
This creates a new Person object with the name "John" and age 30. You can then call the say_hello() method on the person object to print the greeting:
```py
person.say_hello()
```
This will output the following message:
```py
Hello, my name is John and I am 30 years old.
```
In summary, OOP in Python allows you to create classes and objects that encapsulate data and behavior. This can make your code more modular, reusable, and easier to maintain.