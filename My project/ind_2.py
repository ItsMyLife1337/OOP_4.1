#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class Vector3D:
    def __init__(self, x, y, z):
        if not all(isinstance(coord, (int, float)) for coord in (x, y, z)):
            raise ValueError("Координаты вектора должны быть числами")
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def read():
        x = float(input("Введите координату x: "))
        y = float(input("Введите координату y: "))
        z = float(input("Введите координату z: "))
        return Vector3D(x, y, z)

    def display(self):
        print(f"({self.x}, {self.y}, {self.z})")

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot_product(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def compare_length(self, other):
        return self.length() - other.length()

# Пример использования
v1 = Vector3D.read()
v2 = Vector3D.read()

print("Вектор 1:")
v1.display()
print("Вектор 2:")
v2.display()

print("Сумма векторов:")
(v1 + v2).display()
print("Разность векторов:")
(v1 - v2).display()
print("Скалярное произведение векторов:", v1.dot_product(v2))
print("Умножение вектора на скаляр:")
(v1 * 2).display()
print("Сравнение векторов (равенство):", v1 == v2)
print("Длина вектора v1:", v1.length())
print("Длина вектора v2:", v2.length())
print("Сравнение длины векторов (v1 > v2):", v1.compare_length(v2) > 0)
print("Сравнение длины векторов (v1 < v2):", v1.compare_length(v2) < 0)