def multiply_even_numbers(nums):
    """Multiply the even numbers.

        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48

        >>> multiply_even_numbers([3, 4, 5])
        4

    If there are no even numbers, return 1.

        >>> multiply_even_numbers([1, 3, 5])
        1
    """
# if there are no even numbers return the value of one - so we must make the result equal 1 in the first place
    result = 1
# then for each number in nums list we check if the number is even by using modulo to see if it is divisible by 2
    for num in nums:
        # if number is even times it by the current value of result
        if num % 2 == 0:
            result *= num
    return result
