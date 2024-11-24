def get_matrix(n, m, z):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(z)
    print( matrix)
    return  matrix
n = int(input("Введите количество повторов строк: "))
m = int(input("Введите количество повторов столбцов: "))
z = input(f"Введите значение матрицы: ")
print(get_matrix(n, m, z))
if n <= 0:
    print("Данное значение исключено")
elif m <= 0:
    print("Данное значение исключено")
else:
    print("Все условия соблюдены")