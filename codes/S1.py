class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_info(self):
        print(f"Информация о человеке:\nИмя: {self.name}\nВозраст: {self.age}\nПол: {self.gender}")

    def greet(self):
        if self.gender == "муж":
            print(f"Здравствуйте, Г-н. {self.name}!\n")
        elif self.gender == "жен":
            print(f"Здравствуйте, Г-жа. {self.name}!\n")
        else:
            print(f"Здравствуйте, {self.name}!\n")

# Создание "объкетов"
person1 = Person(name='Владимир', age=30, gender='муж')
person1.show_info()
person1.greet()

person2 = Person("Анна", 25, "жен")
person2.show_info()
person2.greet()

person3 = Person("Женя", 20, " ")
person3.show_info()
person3.greet()
