def permute(self, nums):
    """
    Given a list of numbers, returns all possible permutations
        of the numbers.

    :type nums: List[int]
    :rtype: List[List[int]]
    """
    
    if not nums:
        return []
    
    permutations = []
    
    self.backtrack(permutations, nums, [])
    
    return permutations
    

def backtrack(self, permutations, nums, current_combination):
    # if we've exhausted nums, then we've finished the current permutation
    if not nums:
        permutations.append(current_combination)
        return
    
    nums_len = len(nums)
    for i, num in enumerate(nums):
        # make the current combination
        this_combination = current_combination + [num]

        # remove the current number from remaining numbers
        remaining_nums = nums[:i]
        if i + 1 < nums_len:
            remaining_nums += nums[i+1:]
        
        # carry on trying to find a combination
        self.backtrack(permutations, remaining_nums, this_combination)