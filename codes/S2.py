import datetime

today = datetime.date.today()


class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
        # True = 1, False = 0. Если сегодня меньше ДР, то будет -1.

    def show_info(self):
        print(f"Информация о человеке:\nИмя: {self.name}\nВозраст: {self.age}\nДень Рождения: {self.birthday}")

    def celebrate_birthday(self):
        if today.day == self.birthday.day and today.month == self.birthday.month:
            print(f"С Днем Рождения, {self.name}! Сегодня тебе исполнилось {self.age} лет.\n")
        else:
            print("Сегодня не День рождения.\n")


# Создание "объкетов"
person1 = Person('Владимир', datetime.date(1993, 8, 10))
person1.show_info()
person1.celebrate_birthday()

person2 = Person("Анна", datetime.date(1998, 3, 5))
person2.show_info()
person2.celebrate_birthday()

person3 = Person("Елизавета", datetime.date(2003, 3, 12))
person3.show_info()
person3.celebrate_birthday()
