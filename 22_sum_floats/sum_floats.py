def sum_floats(nums):
    """Return sum of floating point numbers in nums.

        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9

        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!

    # isinstance(object, type)
    # traditional for loop

    # total = 0  # a variable to keep track of the sum
    # for num in nums:  # to iterate over each number in the list
    #     # chk if number is a float - why is there a little wavy error line but the code runs?
    #     if isinstance(num, float):
    #         total += num  # add the float number to the sum
    # return total  # return the final sum

    # list comprehension with built in sum() function and isinstance()

    return sum(num for num in nums if isinstance(num, float))
