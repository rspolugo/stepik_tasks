# 8.5 Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.

# x = int(input())
# for i in range(x):
#     print(len(set(input().lower())))

# Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.

x = int(input())
new_set=set()
for i in range(x):
    for j in (input().lower()):
        new_set.add(j)
print(len(new_set))