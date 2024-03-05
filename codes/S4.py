class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def greet(self):
        return f"Привет, меня зовут {self._name} и мне {self._age} лет."


person1 = Person("Елизавета", 20)
print(person1._name)

print(person1.greet())