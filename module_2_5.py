def get_matrix(n, m, value):
    matrix = []                   #создаём список
    for i in range(n):            #устанавливаем колличество строк
        n1 = []
        for x in range(m):        #устонавливаем колличество столбцов
            n1.append(value)      #записываем в заданные строки и столбцы значение
        matrix.append(n1)         #добавляем данные в список
    return matrix


res1 = get_matrix(6, 2, 126)
print(res1)
