first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

if first == second and first == third:
    print("Все значения идентичны!")
elif first == second or first == third:
    print("Количество идентичных значений = 2")
else:
    print("Среди введённых значений нет идентичных!")
