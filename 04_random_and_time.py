import random
import time
import string

# alphabet = "abcdef..."
alphabet = string.ascii_lowercase
print(alphabet)
print()

word = "Kognitywistyka"
for _ in range(10):
    print(random.choice(word))

# ctrl + /
time_start = time.time()
input()
time_end = time.time()
duration = time_end - time_start
print(f'Minęło {duration} sekund.')
print(f'time_start = {time_start}\t time_end = {time_end}')
print('time_start =', time_start, '\t time_end =', time_end)
    # -5 : 5

    # 0 : 1 // * 5 -> 0 : 5 // -5 -> -5 : 0       :(
    # 0 : 1 // * 5 -> 0 : 5 // -10 -> -10 : -5    :(
    # 0 : 1 // * 10 -> 0 : 10 // -5 -> -5 : 5     :)

    # random_number = random.random() * 10 - 5
    # random.random() * szerokość_zakresu + wartość_minimalna
    # 4 : 7         -> random.random() * 3 + 4
    # -1 : 3        -> random.random() * 4 - 1
    # -8 : -5       -> random.random() * 3 - 8
    # -0.7 : 0.3    -> random.random() * 1 - 0.7

    # random.randint(1, 10)
    # random.randrange(1, 10)

    # random_number = random.uniform(-5, 5)
    # random_rounded = round(random_number, 2)
    #
    # # na koniec zajęć Niemiaszku pamiętaj:
    # print(f"{random_number}\tplepleple\tbababebe\t{random_rounded}")

    # print(random_number, "\t", random_rounded)
