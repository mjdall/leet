def single_non_duplicate(nums):
    """
    Given a list of sorted, duplicated numbers,
    finds a single entry that is not duplicated.
    """
    # only one entry, means it's the odd entry
    if len(nums) == 1:
        return nums[0]
    
    prev_n = nums[0]
    set_next = False
    
    
    for n in nums[1:]:
        if not set_next and n != prev_n:
            return prev_n
        
        if set_next:
            prev_n = n
        
        set_next = not set_next
    
    return(nums[-1])