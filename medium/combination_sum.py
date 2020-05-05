def combination_sum(candidates, target):
    """
    Given a list of numbers, finds all possible combinations
        of numbers that sum to the target.

    Numbers can be used multiple times.
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if not candidates:
        return []
    
    combinations = []
    
    # 
    backtrack(combinations, target, candidates, [], 0)
    
    return combinations

def backtrack(combinations, target, candidates, current_list, current_sum):
    # for each number in the remaining candidates
    for i, candidate in enumerate(candidates):
        total = candidate + current_sum

        # if the numbers sum to less than target, backtrack
        if total <  target:
            # note return candidates[i:] to avoid duplicate sets
            backtrack(
                combinations,
                target,
                candidates[i:],
                current_list + [candidate],
                total)
        
        # if the current solution sums to target, add it
        if total == target:
            combinations.append(current_list + [candidate])