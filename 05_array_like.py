# Napisz program poszukujacy najwieksza wartosc w zadanej liscie (bez
# wykorzystania funkcji typu sort!).

import random

how_many = int(input('Dej mie ile liczb losowych wygenerowac: '))
random_numbers = []
for i in range(how_many):
    random_numbers.append(random.randint(1, 100))

print(random_numbers)

current_max = random_numbers[0]
# 1 ver
for i in range(1, len(random_numbers)):
    if random_numbers[i] > current_max:
        current_max = random_numbers[i]

print(current_max)

# 2 ver
for number in random_numbers[1:]:
    if number > current_max:
        current_max = number

print(current_max)

# names = ['Baba', 'Bebe', 'Bubu', 'Byby', 'Bobo']
# salaries = [10000, 1000, 3000, 2500, 8]
# index = list(range(5))     # index = list(range(5))
#
# # [x for _,x in sorted(zip(Y,X))]
# print([name for _, name in sorted(zip(salaries, names))])
# print()
#
# # to samo, ale inaczej:
# for salary, name in sorted(zip(salaries, names)):
#     print(name, end='\t')
# print()
# # pętla sortująca (ręcznie!) zarobki i jednocześnie indeksy
# sorted_salaries = [salaries[0]]
# sorted_index = [index[0]]
#
# # The syntax of the insert() method is list.insert(i, elem)
#
# for i in range(1, len(salaries)):
#     if_appended = False
#     for j in range(0, len(sorted_salaries)):
#         if salaries[i] < sorted_salaries[j]:  # 1000 < 10000
#             # sorted_salaries = sorted_salaries[:j] + [salaries[i]] + sorted_salaries[j:]
#             sorted_salaries.insert(j, salaries[i])
#             # sorted_index = sorted_index[:j] + [index[i]] + sorted_index[j:]
#             sorted_index.insert(j, index[i])
#             if_appended = True
#             break
#     if not if_appended:
#         sorted_salaries.append(salaries[i])
#         sorted_index.append(index[i])
#
# # sorted_salaries = [8, 1000, 2500, 3000, 10000]
# print(sorted_salaries)
# # sorted_index = [4, 1, 3, 2, 0]
# print(sorted_index)
# # posortowana lista imion
# for idx in sorted_index:
#     print(names[idx], end='\t')


# # Stwórz liste zagniezdzona, o wymiarach n x m. n i m powinny byc pobrane z
# # klawiatury. Zawartosc listy powinna byc losowa. Wyswietl otrzymana liste.
# import random
#
# n = int(input('Dej liczbe n: ')) # rows
# m = int(input('Dej liczbe m: ')) # columns
#
# # w petli wewnętrznej będę dodawał losowe elementy do listy,
# # w pętli zewnętrznej będę dodawał powyższe listy do głównej listy
# nested_list = []
# for row in range(n):
#     baby_list = []
#     for cell in range(m):
#         baby_list.append(random.randint(1, 100))
#     nested_list.append(baby_list)
#
# # wyświetlam główną listę
# print(nested_list)
# print()
#
# # ale i w 'pretty mode'
# for row in nested_list:
#     for cell in row:
#         print(cell, end='\t')
#     print()

# names = [['Baba', 10000], ['Bebe', 1000], ['Bubu', 3000], ['Bobo', 2500], ['Byby', 8]]
# salaries = [10000, 1000, 3000, 2500, 8]
# # index = [0, 1, 2, 3, 4]     # list(range(5))
#
# if 23000 in salaries:
#     print('no kurde jest tu tysiac')
# else:
#     print('no motyla noga, nie ma tu tysiaca')
#
# print()
#
# # pętla sortująca (ręcznie!) zarobki i jednocześnie indeksy
# # na wyjściu: index = [4, 1, 3, 2, 0]
# for row in names:
#     for cell in row:
#         print(cell, end='\t| ')
#     print()

# for idx in index:
#     print(names[idx], end=' ')

# empty_list = []
# for i in range(9, -1, -1):
#     empty_list.append(i)
#
# print(empty_list)
# print()
#
# # * list comprehension
# descending_list = [i for i in range(9, -1, -1)]
# print(descending_list)
#
# # * conversion to list
# descending_list = list(range(9, -1, -1))
# print(descending_list)

# descending_list = []
# i = 9
# while i >= 0:
#     descending_list.append(i)
#     i -= 1
# print()
# print(descending_list)

# ptaki_nadmorskie = ['mewa', 'foka', 'jesiotr', 'osioł', 'Beata Kozidrak']
#
# for ptak in ptaki_nadmorskie:
#     print(ptak)
#
# print('\nco zamiast foki')
#
# ptaki_nadmorskie[1] = input()
# #
# # martwy_ptak = input()
# # ptaki_nadmorskie.remove(martwy_ptak)
# # # for i in range(len(ptaki_nadmorskie)):
# # #     print(ptaki_nadmorskie[i], i)
# #
# print()
# for ptak in ptaki_nadmorskie:
#     print(ptak)
# #
# # print()
# # for i, ptak in enumerate(ptaki_nadmorskie):
# #     print(ptak, i)
