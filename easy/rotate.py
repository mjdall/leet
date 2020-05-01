def rotate(nums, k):
    """
    im tired, fix this later, note: done in place
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    clip_len = len(nums)
    k %= clip_len
    
    curr = nums[0]
    shift_to = k
    num_shifts = 0

    while num_shifts < clip_len:
        next_shift = nums[shift_to]
        nums[shift_to] = curr
        curr = next_shift

        if shift_to != 0:
            shift_to += k
            shift_to %= clip_len
        else:
            shift_to = 1

        num_shifts += 1
