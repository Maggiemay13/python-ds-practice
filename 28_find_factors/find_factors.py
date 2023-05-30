def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
# initilize an empty list to store the factors
# iterate from 1 to num
# for each number i in the iteration, check to see if num is divisible by i without a remainder
# The range function creates a range object that represents a sequence of numbers - and it takes three arguments start - stop - step
# in this function we are using two arguments starts at 1 and creates a list to num by using num + 1
# if the division is exact. append i to the list of factors
# after the iteration is complete, return the list of factors

    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors
