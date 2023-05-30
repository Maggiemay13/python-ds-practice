def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
# a and b represent two friends and each friend is made up of a tuple () that contains name, age, and a list of hoobies []
# extract just the hobbies for the friends using set().  sets in python are unordered collections of unigie elements.  the number 2 represents the index number in the tuple.
# if set (a[2]) & set(b[2]): computes the intersection of the two sets of hobbies,  the & operator performs the set intersection which returns a new set of the common elements between the two sets
# if there are common hobbies the code will return true
# if there are no common hobbies the code will return false.

    if set(a[2]) & set(b[2]):
        return True
    else:
        return False
