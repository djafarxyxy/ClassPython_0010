# Tugas Pemrograman Multiplatform
# Class Rectangle - persegi panjang


class Rectangle:
    length = 0
    width = 0

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def circumference(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"rectangle, {self.length} cm long, and {self.width} cm wide"


def main():
    while True:
        try:
            length = int(input("Masukkan panjang (cm): "))
        except ValueError:
            print("Input harus berupa angka!")
            continue
        if length <= 0:
            print("Input tidak boleh 0!")
            continue
        break

    while True:
        try:
            width = int(input("Masukkan lebar (cm): "))
        except ValueError:
            print("Input harus berupa angka!")
            continue
        if width <= 0:
            print("Input tidak boleh 0!")
            continue
        break

    persegi = Rectangle(length, width)

    print(persegi)
    print("Keliling:", persegi.circumference(), "cm")
