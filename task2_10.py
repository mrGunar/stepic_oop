"""
Объявите класс EmailValidator для проверки корректности email-адреса.
Необходимо запретить создание объектов этого класса: при создании
экземпляров должно возвращаться значение None
"""
from string import ascii_letters, digits
import random


class EmailValidator:
    """Class для проверки корректности email-адреса"""
    def __new__(cls):
        return None

    @classmethod
    def check_email(cls, email):
        """возвращает True, если email записан верно и False - в противном случае"""

        if not cls.is_email_str(email):
            return False

        if not cls.check_letters(email):
            return False

        if ".." in email:
            return False

        if cls.check_count(email, "@"):
            first_path, second_path = email.split("@")

            if "." not in second_path:
                return False

            if first_path and second_path:
                if not cls.check_length(first_path, 100) and not cls.check_length(second_path, 50):
                    return False
        else:
            return False

        return True

    @staticmethod
    def check_count(email, letter):
        """Проверка одного @ в email"""
        return email.count(letter) == 1

    @staticmethod
    def check_letters(email):
        """Проверка допустимых симолов"""
        main = ascii_letters + digits + "_.@"
        for letter in email:
            if letter not in main:
                return False
        return True

    @staticmethod
    def check_length(email, length):
        """Проверка длинны частей емейла"""
        return len(email) <= length


    @classmethod
    def get_random_email(cls):
        """для генерации случайного email-адреса по формату:
        xxxxxxx...xxx@gmail.com,
        где x - любой допустимый символ в email (латинский буквы,
        цифры, символ подчеркивания и точка"""
        string = list(ascii_letters + digits + "_.")
        random.shuffle(string)
        string = "".join(string[:random.randint(5, 100)])
        return string + "@gmail.com"

    @staticmethod
    def is_email_str(email):
        """для проверки типа переменной email, если строка, то возвращается
        значение True, иначе - False"""
        return isinstance(email, str)
