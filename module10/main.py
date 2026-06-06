class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter method for name
    def get_name(self):
        return self.__name

    #Setter method for name
    def set_name(self, name):
        self.__name = name

    #Getter method for age
    def get_age(self):
        return self.__age

    #Setter method for age
    def set_age(self, age):
        self.__age = age


#Creating an instance of Student
student1 = Student("Alice", 17)

#Using getter and setter methods
print("Name:", student1.get_name()) #Outpout: Name: Alice
student1.set_name("Bob")
print("Updated Name:", student1.get_name()) #Output: Updated Name:Bob

print("Age:", student1.get_name()) #Output: Age: 17
student1.set_age(18)
print("Updated Age:", student1.get_age()) #Output: Updated Age: 18


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
      self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

circle_1 = Circle(7)
square_1 = Square(10)

print(circle_1.area())
print(square_1.area())