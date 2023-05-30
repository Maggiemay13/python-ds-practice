def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
# iterate each character using the for loop
# if the character, when converted to lowercase, matches the lowercase version of to_swap, we check its case and flip it accordingly.  Otherwise append the character to the result string as is

    result = ""
    for char in phrase:
        if char.lower() == to_swap.lower():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    return result
