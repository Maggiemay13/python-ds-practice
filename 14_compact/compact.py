def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
# use a list comprehension is used to iterate over each element in the input list.  The conditional statment 'if' filters out the elemts that evulate to False in a Boolean context, removing them from the new list

    return [x for x in lst if x]
