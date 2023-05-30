def intersection(l1, l2):
    """Return intersection of two lists as a new list::

        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]

        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]

        >>> intersection([1, 2, 3], [3, 4])
        [3]

        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    # intersection takes two lists as an input and returns a new list that contains the elements that are common to both lists.  the set function is used to convert both l1 and l2 into sets, resulting in a set that contains only the common elements.  Then use list to convert the resulting set back into a list
    return list(set(l1) & set(l2))
