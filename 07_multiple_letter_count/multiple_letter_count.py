def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
# create an empty dict to store the letters from phrase in it
# create a for loop to iterate over each character
# inside the loop the .get() method is used on letter_count to retreive the current count of the letter.  if the letter is not already in letter_count the .get() method returns 0 as a default value
# the letter coutn is updated by th +1
# keeps looping over every letter in phrase until the dict is returned

    letter_count = {}
    for letter in phrase:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count
