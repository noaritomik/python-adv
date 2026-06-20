from abc import ABC, abstractmethod


# =====================================
# Abstract Base Class: Person
# =====================================
class Person(ABC):

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    # Encapsulation
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Weight must be greater than 0.")
        self.__weight = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be greater than 0.")
        self.__height = value

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    @abstractmethod
    def print_info(self):
        pass


# =====================================
# Adult Class
# =====================================
class Adult(Person):

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal Weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def print_info(self):
        print("\n===== Adult Information =====")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} m")
        print(f"BMI: {self.calculate_bmi():.2f}")
        print(f"Category: {self.get_bmi_category()}")


# =====================================
# Child Class
# =====================================
class Child(Person):

    ADJUSTMENT_FACTOR = 0.95

    def calculate_bmi(self):
        bmi = self.weight / (self.height ** 2)
        return bmi * self.ADJUSTMENT_FACTOR

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi < 14:
            return "Underweight"
        elif bmi < 18:
            return "Normal Weight"
        elif bmi < 24:
            return "Overweight"
        else:
            return "Obese"

    def print_info(self):
        print("\n===== Child Information =====")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} m")
        print(f"Adjusted BMI: {self.calculate_bmi():.2f}")
        print(f"Category: {self.get_bmi_category()}")


# =====================================
# BMI Application Class
# =====================================
class BMIApp:

    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def collect_user_data(self):

        while True:
            try:
                print("\n===== BMI SYSTEM =====")

                name = input("Enter name: ")
                age = int(input("Enter age: "))
                weight = float(input("Enter weight (kg): "))
                height = float(input("Enter height (m): "))

                # Automatically decide Adult or Child
                if age >= 18:
                    person = Adult(name, age, weight, height)
                else:
                    person = Child(name, age, weight, height)

                self.add_person(person)

                again = input("\nAdd another person? (y/n): ").lower()

                if again != "y":
                    break

            except ValueError as e:
                print("Error:", e)

    def display_all_people(self):

        if not self.people:
            print("No records found.")
            return

        print("\n========== BMI REPORT ==========")

        for person in self.people:
            person.print_info()


# =====================================
# Main Function
# =====================================
def main():
    app = BMIApp()
    app.collect_user_data()
    app.display_all_people()


if __name__ == "__main__":
    main()