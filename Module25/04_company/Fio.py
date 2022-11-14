# This Python file uses the following encoding: utf-8
import random

name = ['Иван', 'Саша', 'Петя', 'Гоша', 'Гоча', 'Вадим', 'Руслан']
surname = ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Михайлов', 'Лопатин', 'Субботин']
age = [34, 45, 54, 25, 56]


def generate_name():
    return random.choice(name)


def generate_surname():
    return random.choice(surname)


def generate_age():
    return random.choice(age)

