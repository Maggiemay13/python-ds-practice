def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
# convert all letters in the string to lowercase, passing the lowercase letter as the argument
# return the number of thimes the argument occurs
    return word.lower().count(letter.lower())
