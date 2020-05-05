def combination_sum2(candidates, target):
    """
    Given a list of numbers, finds all possible combinations
        of numbers that sum to the target.

    Numbers can only be used once and the cant include dups.
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if not candidates:
        return []
    
    combinations = []
    
    backtrack(combinations, target, candidates, [], 0)
    
    return combinations

def backtrack(combinations, target, candidates, current_list, current_sum):
    """
    """
    candidate_len = len(candidates)
    for i, candidate in enumerate(candidates):
        total = candidate + current_sum

        if total < target:
            # call backtrack if we can possibly make a set
            backtrack(
                combinations,
                target,
                candidates[i+1:],
                current_list + [candidate],
                total)
        
        # if the current set sums to total
        if total == target:
            # check its not already in current combinations, if not, append
            this_combination = sorted(current_list + [candidate])
            if this_combination not in combinations:
                combinations.append(this_combination)