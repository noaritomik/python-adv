class Student:
    def __init__(self, name, percentage):
        self.name=name
        self.percentage=percentage

    def show(self):
        print("My name is:", self.name, "my percentage is:" ,self.percentage)

studenti = Student( "Noar", 65)

studenti.show()
#variabla publike
class MyClass:
    def __init__(self):
        self.public_variable = "This is a public variable"

my_class = MyClass()
print(my_class.public_variable)
#variabla protected
class Klasaime:
    def __init__(self):
        self._protected_variable = "This is a protected variable"

    def _protected_method(self):
        print("This is a protected variable")

klasaime= Klasaime()
print(klasaime._protected_variable)

#variabla private
class one_d:
    def __init__(self):
        self.__private_variable = "This is a private variable"
teacher=one_d()
print(teacher.__private_variable)