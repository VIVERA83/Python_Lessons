"""Напишите функцию, которая принимает целое число в качестве входных данных и возвращает число битов, равное единице в
двоичном представлении этого числа.
Вы можете гарантировать, что входные данные неотрицательны.
Пример: двоичное представление 1234is10011010010, поэтому функция должна возвращать 5в этом случае"""

def countBits(n):
    number = 0
    while n:
        if n % 2:
            number += 1
        n //= 2
    return number

def primer (n): # лучшее решение
    return bin(n).count("1") # bin - преобразует число в двоичную систему, count выводит количество символов

print(countBits(1234))
print(primer(1234))

"""На этот раз никакой истории, никакой теории. В приведенных ниже примерах показано, как написать функциюaccum:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""
def accum (s):
    #s = str(s)
    st = ''
    for i in range(len(s)):
        st += (s[i]+i*s[i]).title()+'-'
    return st[0:-1]

print(accum("abcd"))

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s)) # 'эта штука бехит по списку и возращает индекс и значение


def accum1(s):
    return '-'.join(c.title() + c * i for i, c in enumerate(s)) # 'эта штука бехит по списку и возращает индекс и значение

print(accum1('abcd'))



"""Вам будет дано слово. Ваша задача-вернуть средний символ слова. Если длина слова нечетная, верните средний символ. Если длина слова четная, верните средние 2 символа.

#Kata.getMiddle("test") should return "es"
#Kata.getMiddle("testing") should return "t"
#Kata.getMiddle("middle") should return "dd"
#Kata.getMiddle("A") should return "A"
"""
def get_middle(s):
  #  return [s[len(s)//2] if len(s) % 2 else s[len(s)//2-1:len(s)//2+1]]
  return s[len(s) // 2] if len(s) % 2 else s[len(s) // 2 - 1:len(s) // 2 + 1] # первый раз в одну строчку сделал сам


#        return s[len(s)//2]
#    else:
#        return s[len(s)//2-1:len(s)//2+1]


print(get_middle('middle'))
print(get_middle('testing'))