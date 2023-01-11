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
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Словарь

# dict1 = {}
# dict2 = dict()
# dict1 = dict.fromkeys(['name', 'age', 'job'], 'Missed information')
#
# info_tuple = (['name', 'Timur'], ['age', 28], ['job', 'Teacher'])  # кортеж списков
# info_dict = dict(info_tuple)  # создаем словарь на основе кортежа списков
#
# info_list = [('name', 'Timur'), ('age', 28), ('job', 'Teacher')]  # список кортежей
# info_dict = dict(info_list)  # создаем словарь на основе списка кортежей
#
# keys = ['name', 'age', 'job']
# values = ['Timur', 28, 'Teacher']
#
# info = dict(zip(keys, values))

# Длиной словаря называется количество его элементов. Для определения длины словаря используют встроенную функцию
# len() (от слова length – длина)
#
# Оператор in позволяет проверить, содержит ли словарь заданный ключ
#
# Оператор принадлежности in на словарях работает очень быстро, намного быстрее, чем на списках,
# поэтому если нужен многократный поиск в коллекции данных, словарь – подходящий выбор.
#
# Встроенная функция sum() принимает в качестве аргумента словарь с числовыми ключами и вычисляет сумму его ключей.

# Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке),
# чей номер оканчивается на 8.

# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
# set=set()
# for i in users:
#     if i['phone'][-1]=='8':
#         set.add(i['name'])
# print(*sorted(set))

# Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке),
# у которых нет информации об электронной почте.

# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
# set=set()
# for i in users:
#     if 'email' not in i or i['email']=='':
#         set.add(i['name'])
# print(*sorted(set))

# Напишите программу, которая будет превращать натуральное число в строку, заменяя все цифры в числе на слова:
#
# 0 на zero;
# 1 на one;
# 2 на two;
# 3 на three;
# 4 на four;
# 5 на five;
# 6 на six;
# 7 на seven;
# 8 на eight;
# 9 на nine.

# digits = {
#           '0': 'zero',
#           '1': 'one',
#           '2': 'two',
#           '3': 'three',
#           '4': 'four',
#           '5': 'five',
#           '6': 'six',
#           '7': 'seven',
#           '8': 'eight',
#           '9': 'nine'
#          }
#
# print(*[digits[key] for key in input()])

#Напишите программу, которая по номеру курса выводит информацию о данном курсе

# d = {
#     "CS101": "3004, Хайнс, 8:00",
#     "CS102": "4501, Альварадо, 9:00",
#     "CS103": "6755, Рич, 10:00",
#     "NT110": "1244, Берк, 11:00",
#     "CM241": "1411, Ли, 13:00"
# }
# x = input()
# if x in d:
#     print(x+": "+d[x])

# На мобильных кнопочных телефонах текстовые сообщения можно отправлять с помощью цифровой
# клавиатуры.
# Поскольку с каждой клавишей связано несколько букв,
# для большинства букв требуется несколько нажатий клавиш.
# При однократном нажатии цифры генерируется первый символ,
# указанный для этой клавиши. Нажатие цифры 2, 3, 4 или 5 раз генерирует второй,
# третий, четвертый или пятый символ клавиши.

# d = {
#     ".": '1', ",": '11', "?": '111', "!": '1111', ":": '11111',
#     "a": '2', "b": '22', "c": '222',
#     "d": '3', "e": '33', "f": '333',
#     "g": '4', "h": '44', "i": '444',
#     "j": '5', "k": '55', "l": '555',
#     "m": '6', "n": '66', "o": '666',
#     "p": '7', "q": '77', "r": '777', "s": '7777',
#     "t": '8', "u": '88', "v": '888',
#     "w": '9', "x": '99', "y": '999', "z": '9999',
#     " ": '0'
# }
# for i in input().lower():
#     if i not in d:
#         continue
#     print(d[i], end='')

# Код Морзе для представления цифр и букв использует тире и точки.
# Напишите программу для кодирования текстового сообщения в соответствии с кодом Морзе.

# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# morse_code = dict(zip(letters, morse))
# x= input().upper()
# for symbol in "' ',.+=?!-":
#     if symbol in x:
#         x = x.replace(symbol, '')
#
# for i in x:
#     print(morse_code[i], end=' ')

# методы словарей

# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     result[num] = result.get(num, 0) + 1

# info1 |= info2 - конкатенация
#
# info1 = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
# info2 = {'age': 30,
#         'city': 'New York',
#         'email': 'bob@web.com'}
# info1.update(info2)
# print(info1)

# Метод setdefault() позволяет получить значение из словаря по заданному ключу,
# автоматически добавляя элемент словаря, если он отсутствует.

# С помощью оператора del можно удалять элементы словаря по определенному ключу.

# Метод popitem() удаляет из словаря последний добавленный элемент и возвращает удаляемый элемент в виде кортежа (ключ, значение).

# Дополните приведенный код, чтобы в переменной result хранился словарь,
# в котором ключи – числа от 1 до 15 (включительно),
# а значения представляют собой квадраты ключей.

# result = {}
# keys=[]
# values=[]
#
# for i in range(1,16):
#     x=i*i
#     keys.append(i)
#     values.append(x)
# result=dict(zip(keys,values))
# print(result)
# # or
# result2=dict(zip([i for i in range(1,16)], [i**2 for i in range(1,16)]))
# print(result2)

# Дополните приведенный код так, чтобы в переменной result хранился словарь,
# в котором для каждого символа строки text будет подсчитано количество его вхождений.

# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# list = list(text)
# result = {}
# for letter in list:
#     result[letter]=result.get(letter, 0)+1
# print(result)

# Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s.
# Если таких слов несколько,
# должно быть выведено то, что меньше в лексикографическом порядке.

# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
# result = {}
# max = 0
# for i in s.split():
#     result[i] = result.get(i, 0) + 1
#     if result[i] > max:
#         max = result[i]
# l = list()
# for i in result:
#     if max == result[i]:
#         l.append(i)
# l.sort()
# print(l[0])

# Вам доступен список pets, содержащий информацию о собаках и их владельцах.
# Каждый элемент списка – это кортеж вида (кличка собаки, имя владельца,
# фамилия владельца, возраст владельца).
#
# Дополните приведенный код так, чтобы в переменной result хранился словарь,
# в котором для каждого владельца будут перечислены его собаки.
# Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца),
# а значением – список кличек собак (сохранив исходный порядок следования)

# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
# result = {}
# for i in pets:
#     result.setdefault(i[1:4], []).append(i[0])
# print(result)