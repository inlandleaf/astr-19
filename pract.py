class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

# def pract_func():
#     name = "Zach"
#     print(f"My name is {name}")

if __name__ == "__main__":
    person = Person("Zach", 21)
    person.describe()