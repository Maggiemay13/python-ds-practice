def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """

# if the value of num is less then 0 or if num is not an integer, the function returns none to indicate an illegal value of num
# isinstance is a built in function that allows you to check the type of an object - takes two arguments the object you want to check and the type you want to check against
# not keyword is a logical operator in python that is used to reverse a boolean value
# if the value of num is 0 the function returns as empty string since no repetition is needed.
# otherwise the function uses the multiplication operator to repeat yjr phrase num times and returns the result

    if not isinstance(num, int) or num < 0:
        return None
    return phrase * num
