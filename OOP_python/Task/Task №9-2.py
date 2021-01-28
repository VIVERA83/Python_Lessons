# 2. Напишите класс Matrix для работы с матрицами. Реализуйте перегрузку операторов сложения и вычитания для матриц
# равных размеров. Перегрузите оператор умножения для матриц, которые могут быть перемножены. Также сделайте
# возможность сравнения матриц между собой (на равенство и неравенство).

class Matrix:

    def __init__(self, matrix: list):
        try:
            if not all([isinstance(value, (int, float)) for items in matrix for value in items]):
                raise TypeError("Матрица должна быть типа Int или float")
        except:
            raise TypeError("Параметр matrix должен быть типа List")
        self.__height = len(matrix)
        if not all([len(item) == self.__height for item in matrix]):
            raise ValueError("Матрица не является прямоугольной")
        self.__width = len(matrix[0])
        self.__matrix = matrix

    @property
    def getMatrix(self):
        return self.__matrix

    def check(self):
        def wrapper(*matrix):
            if not isinstance(matrix[1], Matrix):
                raise TypeError("Передаваемы параметры должны быть типа Matrix")
            if not all([matrix[0].__width == matrix[1].__width, matrix[0].__height == matrix[1].__height]):
                raise ValueError("Матрицы должны быть симметричны")
            return self(matrix[0], matrix[1])

        return wrapper

    @check
    def __add__(self, other):
        return Matrix(
            [[self.__matrix[i][j] + other.__matrix[i][j] for j in range(self.__width)] for i in range(self.__height)])

    def __iadd__(self, other):
        return self.__add__(other)

    @check
    def __sub__(self, other):
        return Matrix(
            [[self.__matrix[i][j] - other.__matrix[i][j] for j in range(self.__width)] for i in range(self.__height)])

    def __isub__(self, other):
        return self.__sub__(other)

    @check
    def __mul__(self, other):
        return Matrix(
            [[self.__matrix[i][j] * other.__matrix[i][j] for j in range(self.__width)] for i in range(self.__height)])

    def __imul__(self, other):
        return self.__mul__(other)

    @check
    def __eq__(self, other):
        return all([it1 == it2 for (it1, it2) in zip(self.__matrix, other.__matrix)])

    def __ne__(self, other):
        return not self.__eq__(other)


m = [[i for i in range(4)] for j in range(1, 5)]
n = [[i for _ in range(4)] for i in range(1,5)]

for (it1, it2) in zip(m, n):
    print(f"{it1}     {it2}")

# m[1].extend([1,2])
print(m)
ar1 = Matrix(m)
ar2 = Matrix(n)
alignment = 40

print('Сложение матриц (ar1 + ar2).getMatrix'.ljust(alignment), (ar1 + ar2).getMatrix)
ar1 += ar2
print('Сложение через ar1 += ar2'.ljust(alignment), ar1.getMatrix)

print('Вычитание матриц (ar1 - ar2).getMatrix'.ljust(alignment), (ar1 - ar2).getMatrix)
ar1 -= ar2
print('Вычитание через ar1 -= ar2'.ljust(alignment), ar1.getMatrix)

print('Умножение (ar1 * ar2).getMatrix'.ljust(alignment), (ar1 * ar2).getMatrix)
ar1 *= ar2
print('Умножение через ar1 *= ar2'.ljust(alignment), ar1.getMatrix)
print('Сравнение на равенство ar1 == ar2'.ljust(alignment), ar1 == ar2, ar1.getMatrix)
print('Сравнение на неравенство ar1 != ar2'.ljust(alignment), ar1 != ar2, ar2.getMatrix)
