def atoi(s):
    """
    Parses a string to an integer.
    Leading whitespace is trimmed.
    + or - at the start of a number are ok.
    Words at the end of the parsed number are ok.
    If a character is encountered before a number (or +-), the string won't be parsed.

    :type s: str
    :rtype: int
    """
    # remove leading white space
    s = s.lstrip()

    # get any sign if there is one
    sign = 1
    if s[0] in { '-', '+' }:
        sign = -1 if s[0] == '-' else 1
        s = s[1:]

    # num parses holds how many characters can be parsed
    # to an int
    num_parses = 0

    for i in range(0, len(s)):
        # try parse current character to a string
        try:
            int(s[i])
        except ValueError:
            # break if parse fails
            break

        num_parses += 1

    # no numbers could be parsed
    if num_parses == 0:
        return 0

    # return the final number
    return sign * int(s[:num_parses])