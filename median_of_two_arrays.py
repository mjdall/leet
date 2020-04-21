def find_median_sorted_arrays(nums1, nums2):
        """
        There are two sorted arrays nums1 and nums2 of size m and n respectively.
        Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
        You may assume nums1 and nums2 cannot be both empty.
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        median_position = ((nums1_len + nums2_len) / 2)
        median_numbers = [median_position]
        if (nums1_len + nums2_len) % 2 == 0:
            median_numbers.insert(0, median_position - 1)

        n1_idx = 0
        n2_idx = 0
        curr_position = 0
        found_numbers = []
        curr_number = None
        med_set = set(median_numbers)
        
        while curr_position <= median_numbers[-1]:
            n1 = nums1[n1_idx] if n1_idx < nums1_len else None
            n2 = nums2[n2_idx] if n2_idx < nums2_len else None

            if (n1 <= n2 and n1 is not None) or n2 is None:
                n1_idx += 1
                curr_number = n1
            else:
                n2_idx += 1
                curr_number = n2

            if curr_position in med_set:
                found_numbers.append(curr_number)
                
            curr_position += 1

        return float(sum(found_numbers)) / len(found_numbers)
