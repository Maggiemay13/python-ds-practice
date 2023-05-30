def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.

        >>> triple_and_filter([1, 2, 3, 4])
        [12]

        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]

        >>> triple_and_filter([1, 2])
        []
    """
# traditional loop
    # tripled_list = []
    # for num in nums:
    #     if num % 4 == 0:
    #         tripled_list.append(num * 3)
    # return (tripled_list)

# list comprehension
    return [num * 3 for num in nums if num % 4 == 0]


# the triple_and_filter function take sone argument 'nums' which represents a list of numbers
# this function returns a new list with the values trippled of only those nu,bers in the original list that are divisible by 4

# iterate over each number in the nums list
# check if they are divisable by four
# if the number is divisible by four , triple its value
# add the tripled value to the new list
# Return the new list containing the tripled values of the numbers that were are divisible by four
