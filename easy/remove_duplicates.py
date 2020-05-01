def remove_duplicates(nums):
        """
        Remove duplicates in place, nums is sorted w/possible duplicates.
        Return int denoting the length of sorted elements in nums.
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # the number for the next number to be shifted to
        set_pos = 1

        # the previous number, to check for duplicate
        prev = nums[0]
        
        for i in range(1, len(nums)):
            curr = nums[i]

            # if current number isnt same as previous, update nums
            # in place and incremement set pos
            if prev != curr:
                nums[set_pos] = curr
                set_pos += 1

            # update prev element
            prev = curr

        # set pos holds the length of sorted elements as it's 1 ahead of
        # the position being set
        return(set_pos)
