# 8.5 Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.

# x = int(input())
# for i in range(x):
#     print(len(set(input().lower())))

# Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.

# x = int(input())
# new_set=set()
# for i in range(x):
#     for j in (input().lower()):
#         new_set.add(j)
# print(len(new_set))

# Напишите программу для определения общего количества различных слов в строке текста.

# s = input().lower().split()
# # print(s)
# # for i in range (len(s)):
# #     s[i]=s[i].strip('.,;:-?!')
# # print(s)
# # set_words= set(s)
# # print(s)
# # print(len(set_words

# На вход программе подается строка текста, содержащая числа. Для каждого числа выведите слово YES (в отдельной строке),
# если это число ранее встречалось в последовательности или NO, если не встречалось.

# s = input().split(' ')
# print(len(s))
# set =(s)
# for i in range(len(s)):
#     s[i] = int(s[i])
#     if s[i] in set:
#         print('YES')
#     else:
#         print('NO')

# A | B
# A.union(B)
# Возвращает множество, являющееся объединением множеств A и B
# A |= B
# A.update(B)
# Добавляет в множество A все элементы из множества B
# A & B
# A.intersection(B)
# Возвращает множество, являющееся пересечением множеств A и B
# A &= B
# A.intersection_update(B)
# Оставляет в множестве A только те элементы, которые есть в множестве B
# A - B
# A.difference(B)
# Возвращает разность множеств A и B
# A -= B
# A.difference_update(B)
# Удаляет из множества A все элементы, входящие в B
# A ^ B
# A.symmetric_difference(B)
# Возвращает симметрическую разность множеств A и B
# A ^= B
# A.symmetric_difference_update(B)
# Записывает в A симметрическую разность множеств A и B

# На вход программе подаются две строки текста, содержащие числа. Напишите программу,
# которая определяет количество чисел, которые есть как в первой строке, так и во второй.

# x = set(input().split(' '))
# y = set(input().split(' '))
# z = x&y
# print(len(z))

# На вход программе подаются две строки текста, содержащие числа.
# Напишите программу, которая выводит все числа в порядке возрастания, которые есть как в первой строке, так и во второй.

# x = set(int(i) for i in input().split(' '))
# y = set(int(i) for i in input().split(' '))
# z = x&y
# print(*sorted(z))

# На вход программе подаются две строки текста, содержащие числа.
# Напишите программу, которая выводит все числа в порядке возрастания, которые есть в первой строке, но отсутствуют во второй.

# x = set(int(i) for i in input().split(' '))
# y = set(int(i) for i in input().split(' '))
# z= x-y
# print(*sorted(z))

# На вход программе подается натуральное число nn, а затем nn различных натуральных чисел, каждое на отдельной строке.
# Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.

# n = int(input())
# list_of_digits =[set(input()) for _ in range(n)]
# zero_element = list_of_digits[0]
#
# for i in range(1,len(list_of_digits)):
#     zero_element.intersection_update(list_of_digits[i])
#
# print(*sorted(zero_element))

# Подмножества и надмножества

# set1 <= set2
# set1.issubset(set2)
# Возвращает True, если set1 является подмножеством set2
# set1 >= set2
# set1.issuperset(set2)
# Возвращает True, если set1 является надмножеством set2
# set1 < set2
# Эквивалентно set1 <= set2 and set1 != set2 (строгое подмножество)
# set1 > set2
# Эквивалентно set1 >= set2 and set1 != set2 (строгое надмножество)

# На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры

# n, m = set(input()), set(input())
# if n.isdisjoint(m) == True:
#     print('NO')
# else:
#     print('YES')

# На вход программе подаются два числа.
# Напишите программу, которая определяет, входят ли в запись первого числа все цифры,
# содержащиеся в записи второго (независимо от повтора, то есть количества цифр) числа или нет.

# n, m = set(input()), set(input())
# if n.issubset(m) == True:
#     print('NO')
# else:
#     print('YES')

# Даны по 10-балльной шкале оценки по информатике трех учеников.
# Напишите программу, которая выводит множество оценок, которые есть и у первого и у второго учеников, но которых нет у третьего ученика

# x = set(int(i) for i in input().split(' '))
# y = set(int(i) for i in input().split(' '))
# z = set(int(i) for i in input().split(' '))
#
# cross_xy = (x&y)-z
# print(*sorted(cross_xy, reverse=True))

# Даны по 10-балльной шкале оценки по математике трех учеников.
# Напишите программу, которая выводит множество оценок, имеющихся у учеников, которые встречаются не более, чем у двух из указанных учеников.

# one = set(int(i) for i in input().split(' '))
# two = set(int(i) for i in input().split(' '))
# three = set(int(i) for i in input().split(' '))
#
# print(*sorted((one|two|three)-(one&two&three)))

# Даны по 10-балльной шкале оценки по физике трех учеников.
# Напишите программу, которая выводит множество оценок третьего ученика,
# которые не встречаются ни у первого, ни у второго ученика.

# one = set(int(i) for i in input().split(' '))
# two = set(int(i) for i in input().split(' '))
# three = set(int(i) for i in input().split(' '))
#
# print(*sorted(three-(one|two), reverse=True))

# Даны по 10-балльной шкале оценки по биологии трех учеников.
# Напишите программу, которая выводит множество оценок,
# не встречающихся ни у одного из трех учеников.

# one = set(int(i) for i in input().split(' '))
# two = set(int(i) for i in input().split(' '))
# three = set(int(i) for i in input().split(' '))
#
# four = set(int(i) for i in range(11))
# print(*sorted(four-(one|two|three)))

# Используя генератор множеств, дополните приведенный код так,
# чтобы получить множество, содержащее уникальные значения списка items.
# Результат вывести на одной строке, в упорядоченном виде,
# разделяя элементы одним символом пробела.

# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# set=set(int(d) for d in items)
# print(*sorted(set))

# Используя генератор множеств, дополните приведенный код так,
# чтобы получить множество, содержащее первую букву каждого слова (в нижнем регистре) списка words.
# Результат вывести на одной строке в алфавитном порядке, разделяя элементы одним символом пробела.

# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
# set = set(i[0].lower() for i in words)
# print(*sorted(set))

# Используя генератор множеств, дополните приведенный код так, чтобы получить множество,
# содержащее уникальные слова (в нижнем регистре) строки sentence.
# Результат вывести на одной строке в алфавитном порядке, разделяя элементы одним символом пробела.

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
#
# set = set(i.strip(':,.!?();').lower() for i in sentence.split())
# print(*sorted(set))

# Используя генератор множеств, дополните приведенный код так, чтобы получить множество, содержащее уникальные слова  строки sentence длиною меньше 4 символов.
# Результат вывести на одной строке (в нижнем регистре) в алфавитном порядке, разделяя элементы одним символом пробела.

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
#
# set = set(i.strip('()!?/.,:;').lower() for i in sentence.split() if len(i.strip('()!?/.,:;')) < 4)
# print(*sorted(set))

# Используя генератор множеств, дополните приведенный код так, чтобы он выбрал из списка files уникальные имена файлов c расширением .png, независимо от регистра имен и расширений.
# Имена файлов вывести вместе с расширением, все на одной строке, в нижнем регистре, в алфавитном порядке через пробел.

# files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
# set2 = set(i.lower() for i in files if i.lower().endswith('.png'))
# print(*sorted(set2))

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Кортеж (тип tuple) – неизменяемая версия списка (тип list), а замороженное множество (тип frozenset) – неизменяемая версия обычного множества (тип set).

