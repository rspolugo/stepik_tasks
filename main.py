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