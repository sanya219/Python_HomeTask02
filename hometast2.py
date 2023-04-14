# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def task1():
    print("Задача 1")
    number = abs(int(input("Введите N: ")))
    for i in range(1, number + 1):
        print(f"{factorial(i)}", end = "\t")

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
def task2():
    print("Задача 2")
    print("X | Y | Z | ¬(X ∧ Y) ∨ Z")
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                print(f"{x} | {y} | {z} | {int(not(x and y) or z)}")









#task1()
task2()