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
    print("\nЗадача 2")
    print("X | Y | Z | ¬(X ∧ Y) ∨ Z")
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                print(f"{x} | {y} | {z} | {int(not(x and y) or z)}")

# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2
def task3():
    print("\nЗадача 3")
    string1 = input("Введите первую строку: ")
    string2 = input("Введите вторую строку: ")
    for i in string1:
        print(f"'{i}' = {countChars(i, string2)}")

def countChars(chr, text):
    count = 0
    for i in text:
        if i == chr:
            count += 1
    return count

# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]
def task4():
    print("\nЗадача 4")
    number = abs(int(input("введите число N: ")))
    shiftPos = 2
    lst = list(range(-number, number + 1))
    lst = shiftElementsRight(lst, shiftPos)
    print(lst)

def shiftElementsRight(lst, positions):
    return lst[-positions:] + lst[:-positions]


task1()
task2()
task3()
task4()