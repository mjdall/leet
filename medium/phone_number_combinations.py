def letterCombinations(digits):
    """
    Generates all possible character combinations given an input
        string containg digits 2-9 (inclusive).
    Character combinations are based on old phones lol.
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []
    
    # could have done this in a function rather than an arg
    digit_mapping = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }
    
    combinations = []
    backtrack(digit_mapping, combinations, digits, '')

    return combinations
    
def backtrack(digit_mapping, combinations, digits, curr_str):
    """
    Back tracks the possible phone character combinations.
    """
    if len(digits) <= 0:
        combinations.append(curr_str)
        return()
    
    # for each mapping call backtrack with the one of the char
    # options for the current digits
    for char in digit_mapping[digits[0]]:
        backtrack(
            digit_mapping,
            combinations,
            digits[1:],
            curr_str + char)
