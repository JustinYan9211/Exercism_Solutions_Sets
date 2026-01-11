def digit_count(number):
    number = abs(number)
    if number == 0:
        return 1

    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count


def armstrong_sum(number):
    power = digit_count(number)
    total = 0
    n = abs(number)

    while n > 0:
        total = total + (n % 10) ** power
        n //= 10
    return total
    
def is_armstrong_number(number):
    return armstrong_sum(number) == number
