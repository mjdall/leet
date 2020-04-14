def move_zeros(self, nums):
        """
        Moves all zeros to the end of a list, in place.
        """
        num_nums = len(nums)
        encountered_zeros = 0

        for i in range(0, num_nums):
            num = nums[i]
            if num == 0:
                encountered_zeros += 1
                continue
            nums[i - encountered_zeros] = num

        for i in range(1, encountered_zeros + 1):
            nums[num_nums - i] = 0
