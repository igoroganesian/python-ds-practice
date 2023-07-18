def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    lower = to_swap.lower()
    upper = to_swap.upper()
    final = ''

    for letter in phrase:
        if letter == lower:
           letter = letter.upper()
           final += letter
        elif letter == upper:
             letter = letter.lower()
             final += letter
        else:
            final += letter

    return final