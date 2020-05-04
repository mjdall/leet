def generateParenthesis(n):
        """
        Generate all n possible combinations of valid paranthesis pairs.

        :type n: int
        :rtype: List[str]
        """
        braces = []
        backtrack(braces, '', 0, 0, n)
        return braces

      
def backtrack(braces, current_string, open_braces, closed_braces, max_pairs):
    """
    This was my first backtrack problem, quite interesting.
    Recursively exhausts possible decisions.
    """
    # currently generated string is at max length, so append it
    if (len(current_string) / 2) == max_pairs:
        braces.append(current_string)
        return
    
    # if we can add more open braces, add an open brace
    if open_braces < max_pairs:
        backtrack(braces, current_string + '(', open_braces + 1, closed_braces, max_pairs)
    
    # if we have less closed braces than open braces we can close an open brace
    if closed_braces < open_braces:
        backtrack(braces, current_string + ')', open_braces, closed_braces + 1, max_pairs)
