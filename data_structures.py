def factorial(number):
    return 1 if number == 1 else number * factorial(number - 1)


def sum_numbers(number):
    return 0 if number == 0 else number + sum_numbers(number - 1)


def countdown(limit):
    print(limit)
    return 1 if limit == 1 else limit - countdown(limit - 1)
countdown(10)
