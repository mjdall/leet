def count_elements(arr):
        """
        Given an integer array arr, count element x such that x + 1 is also in arr.
        If there're duplicates in arr, count them seperately.
        :type arr: List[int]
        :rtype: int
        """
        if arr is None or len(arr) == 0:
            return 0
        
        found_numbers = {}
        for num in arr:
            found_numbers.setdefault(num, 0)
            found_numbers[num] += 1

        nums_in_arr = found_numbers.keys()

        total_count = 0

        for num in nums_in_arr:
            if num + 1 in found_numbers:
                total_count += found_numbers[num]

        return total_count
