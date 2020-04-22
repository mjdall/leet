def product_except_self(nums):
        """
        Given an array nums of n integers where n > 1, 
        return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
        :type nums: List[int]
        :rtype: List[int]
        """
        left_products = [nums[0]]
        right_products = [nums[-1]]
        output = []
        n_nums = len(nums)
        
        for i in range(1, n_nums-1):
            left_products.append(left_products[-1] * nums[i])
            right_products.append(right_products[-1] * nums[n_nums - i - 1])

        n_results = len(left_products)
        
        output = [right_products[-1]]

        for i in range(0, n_results-1):
            output.append(left_products[i] * right_products[n_results-i-2])
            
        output.append(left_products[-1])
        return output
