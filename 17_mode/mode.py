def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # create an empty dictionary to keep track of the counts of each number.
    # use max_count to keep track of the maximum count encountered so far
    # use mode_num to store the current mode number

    # iterate over each number num in the input list.  if num is already in the count dictionary we icrement its count by 1.  Otherwise we add num to the dictionary with a count of 1
    # after updating the count we check if the count of num is greater than max_count.  if it is update max_count and set mode_num to the current num

    # return mode_num

    count = {}
    max_count = 0
    mode_num = None

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

        if count[num] > max_count:
            max_count = count[num]
            mode_num = num

    return mode_num
