# 1
import time
print("""Дан картеж:
    "+792345678", "+792345478", "+792355678", "+592345678", "+392345678", "+7923456558"
    Нужно вывести все номера, начинающие с +7""")


a = ("+792345678", "+792345478", "+792355678", "+592345678", "+392345678", "+7923456558")
for x in a:
    if "+7" in x:          #[:2]ил так как просмотр будет вестись толко в начаде
        print(x)

# 2

print(""" Имеется набор оценок в виде строки:
          "Оценки: 5, 4, 3, 4, 2, 4, 5, 4" 
          Необходимо создать картеж, в котором находились бы только оценки  в виде чиселЖ
          (5, 4, 3, 4, 2, 4, 5, 4) """)

string1 = "Оценки: 5, 4, 3, 4, 2, 4, 5, 4"
a = ()
string1 = string1[string1.find(':')+1:].replace(' ','') # меняем строку, создаем без "оценки:", удаляем пробелы
print(string1)
for i in range(0,len(string1),2) :
    a = a + (int(string1[i]),)
print(a)

# 3
print("""\n Вывести значение картежа:
      ((1,2,3),(4,5,6),(7,8,9))
      в виде таблици:
      1-2-3
      4-5-6
      7-8-9 """)
a = ((1,2,3),(4,5,6),(7,8,9))
for x in a :
    print(x[0], x[1], x[2], sep='-')

# Чужой код Wolf
print('чужой код')
marks = "Оценки: 5 4 3 4 3 5"
marks = marks.split()
marks = marks[1:]
n = len(marks)
for i in range(n):
    marks[i] = int(marks[i])

c = tuple(marks)
print(c)
