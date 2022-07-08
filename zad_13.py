import timeit
from time import process_time


def perfect_number(number):
    sum_of_factors = 0
    for i in range(1, number):
        if number % i == 0:
            print(i)
            sum_of_factors += i
    return sum_of_factors == number
    print(sum_of_factors)


def timeit_decorator(fun):
    t = process_time()
    fun
    print("czas wykonywania funkcji: ", t)



timeit_decorator(perfect_number(33550336))
