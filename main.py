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

# На вход программе подается строка, содержащая строки-идентификаторы.
# Напишите программу, которая исправляет их так,
# чтобы в результирующей строке не было дубликатов.
# Для этого необходимо прибавлять к повторяющимся идентификаторам постфикс _n,
# где n – количество раз, сколько такой идентификатор уже встречался.
#
# string = input().lower().split()
# d = {}
#
# for i in string:
#     d[i]=d.get(i,0)+1
#
#     if i in d:
#         print(f'{i}_{d[i]}', end=' ')
#     else:
#         print(i, end=' ')
# info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
#         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
#         'emp3': {'name': 'Rustam', 'job': 'Tester'}}
# for i in info:
#     print(i)
#     for j in info[i]:
#         print(j + ':', info[i][j])

# x=[2,5,8]
# c={i:2*i for i in x}
# print(c)

# Дополните приведенный код, используя генератор, так чтобы получить словарь result,
# в котором ключом будет позиция числа в списке numbers (начиная с 00),
# а значением – его квадрат.

# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
# result = {i: numbers[i]**2 for i in range(len(numbers))}
# print(result)

# Дополните приведенный код, используя генератор, чтобы получить словарь result,
# состоящий из всех элементов словаря colors, кроме тех, у которых значением является None

# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
# result = {i:colors[i] for i in colors if colors[i]!=None}
# print(result)

# Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря favorite_numbers , значения которых являются двузначными числами

# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
# result = {v: favorite_numbers[v] for v in favorite_numbers if len(str(favorite_numbers[v]))==2}
# print(result)

# Дополните приведенный код, используя генератор, так, чтобы получить словарь result, состоящий из всех элементов словаря months , в которых ключ и значение поменялись местами.

# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
# result = {v: k for k, v in months.items()}
# print(result)

# В переменной s хранится строка пар число:слово. Дополните приведенный код, используя генератор, чтобы получить словарь result , в котором числа будут ключами, а слова – значениями.

# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
# spl=s.split(' ')
# list=[]
# numbers=[]
# letters=[]
# for i in spl:
#     list.append(i.split(':'))
# for j in range(len(list)):
#     numbers.append(list[j][0])
#     letters.append(list[j][1])
#
# temp = dict(zip(numbers, letters))
#
# result={int(k): v for k, v in temp.items()}
#
# print(result)

# or

# result = {int(k):v for k, v in [l.split(':') for l in s.split()]}

# Используя генератор, дополните приведенный код, чтобы получить словарь result,
# где ключом будет элемент списка numbers, а значением – отсортированный по возрастанию список всех его делителей начиная с 1

# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
#
# result={num: [dev for dev in range(1, num+1) if num % dev == 0] for num in numbers}
# print(result)

# Дополните приведенный код, используя генератор, так, чтобы получить словарь result , в котором ключом будет строка – элемент списка words,
# а значением – список соответствующих кодов ASCII символов данной строки

# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
# result = {k:[ord(i) for i in k] for k in words}
# print(result)

# Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря letters ,
# за исключением тех, ключи которых есть в списке remove_keys

# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
# result = {k:v for k,v in letters.items() if k not in remove_keys}
# print(result)

# В переменной students хранится словарь, содержащий информацию о росте (в см) и весе (в кг) студентов.
# Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря students, где указан рост больше
# 167 см, а вес меньше 75 кг.

# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
# result = {k:v for k,v in students.items() if v[0]>167 and v[1]<75}
# print(result)

# Список tuples содержит кортежи, состоящие из трех чисел.
# Дополните приведенный код, используя генератор, чтобы получить словарь result, в котором ключом является первый элемент каждого кортежа,
# а значением – кортеж из оставшихся двух элементов.

# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
# result = {k[0]: k[1:] for k in tuples}
# print(result)

# Даны три списка student_ids, student_names, student_grades, содержащие информацию о студентах.
# Дополните приведенный код, используя генератор, так чтобы получить список result,
# содержащий вложенные словари в соответствии с образцом: [{'S001': {'Camila Rodriguez': 86}}, {'S002': {'Juan Cruz': 98}},...]

# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
# result = [{a: {b: c}} for a, b, c in zip(student_ids, student_names, student_grades)]
# print(result)

# Напишите программу, которая с помощью модуля random моделирует броски монеты.
# Программа принимает на вход количество попыток и выводит результаты бросков: Орел или Решка (каждое на отдельной строке)

# import random
# n = int(input())
# for i in range(n):
#     num = random.randrange(0, 2)
#     if num == 0:
#         print("Орел")
#     else:
#         print("Решка")

