def fib(x):  # функция вычисления фибоначи
    s1, s2 = 0, 1
    for i in range(x - 1):
        s2, s1 = s1 + s2, s2
    return s2


# бинарный поиск собственного изобретения

data = [2313, 7, -1, 231, 2, 31, 23, 5, 0, -5, 5, 7, 23, 6, 3, 8, 2, -555, 445, 45, 3]
d = [1, 2, 5, 7, 9]
q = []


def findbi(lst, n):
    def fin(lst, n, i):
        x = len(lst)
        index = len(lst) // 2
        print(f'i={i}, index={index}, lst[index]={lst[index]}, lst={lst}')

        if not index:
            return [i, lst[index]]
        if lst[index] > n:
            x = fin(lst[:index], n, x)
        elif lst[index] < n:
            x = fin(lst[index:], n, x)
        return x

    res = fin(lst, n, len(lst))

    return res


data.sort()

print(findbi(d, 99))
# print(data[findbi(d,99)])
