def palindrom(word):
    return word == word[::-1]

print(palindrom('bajka'))
print(palindrom('kajak'))

# # maksimum, minimum listy
# import random
#
# def maksimum(lista):
#     """
#     Funkcja zwracająca maksymalny element wejściowej listy.
#     """
#     element_maks = lista[0]
#     for element in lista[1:]:
#         if element > element_maks:
#             element_maks = element
#     return element_maks
#
# test_list = []
# for _ in range(10):
#     test_list.append(random.randint(-100, 100))
# print(test_list)
#
# wynik = maksimum(test_list)
# print(wynik)

# def get_square(number):
#     """
#     bababebe
#     """
#     output = number ** 2
#     return output
#
# user_number = int(input("Podaj prosze liczbe, a ją skwadracę: "))
# print(get_square(user_number))
