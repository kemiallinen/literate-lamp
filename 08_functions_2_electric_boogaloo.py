def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1


print(factorial(3))

# def sumowanie_rekurencyjne(lista_liczb, depth=0):
#     if len(lista_liczb) > 0:
#         wynik = lista_liczb[0] + sumowanie_rekurencyjne(lista_liczb[1:], depth=depth+1)
#         print(f'Wynik na poziomie zagnieżdżenia {depth} = {wynik}')
#         return wynik
#     else:
#         return 0
#
# print(sumowanie_rekurencyjne([1, 2, 3, 4, 5]))


# def lutuj_gwiazdki(ile_gwiazdek):
#     if ile_gwiazdek > 0:
#         print('*')
#         lutuj_gwiazdki(ile_gwiazdek - 1)
#
# lutuj_gwiazdki(5)
