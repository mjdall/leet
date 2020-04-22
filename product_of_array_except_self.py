def product_except_self(nums):
        """
        Given an array nums of n integers where n > 1, 
        return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

        Solution involves calculating the product of the numbers, starting from the left side
            of the array, to the right side, as well as the product going in the reverse direction.
        The product at n[i] is the product of the left side multiplied by the product of the right side.
        :type nums: List[int]
        :rtype: List[int]
        """
        # arrays for storing products at each step
        left_products = [nums[0]]
        right_products = [nums[-1]]

        # output array and length of input array
        output = []
        n_nums = len(nums)
        
        # go over the array
        for i in range(1, n_nums-1):
            # calculate forward direction product
            left_products.append(left_products[-1] * nums[i])

            # calculate backward direction product
            right_products.append(right_products[-1] * nums[n_nums - i - 1])

        # the length of the resulting array
        n_results = len(left_products)
        
        # the first insance is the final product in the reverse direction
        output = [right_products[-1]]

        # go over each element except the first and last
        for i in range(0, n_results-1):
            # append the product of the left and right products
            output.append(left_products[i] * right_products[n_results-i-2])
        
        # finally, append the forward direction product and return
        output.append(left_products[-1])
        return output
