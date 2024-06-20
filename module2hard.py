import random

def pass_gen(n):
    result = ""
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result

# Пример использования
n = random.randint(3, 20)
print(f"Число из первой вставки: {n}")
result = pass_gen(n)
print(f"Нужный пароль: {result}")
