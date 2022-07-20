
def perfect_number(number):
    sum_of_factors = 0
    for i in range(1, number):
        if number % i == 0:
            print(i)
            sum_of_factors += i
    return sum_of_factors == number
    print(sum_of_factors)


print(perfect_number(33550336))
