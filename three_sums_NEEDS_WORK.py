def three_sums(nums):
        """
        For finding unique 3 number combinations that sum to zero givens array nums.
        Still not optimised for best performance.
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        found_sets = {}
        combinations = []

        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:-1]):
                remaining_number = -(num1 + num2)
                if remaining_number not in set(nums[i+j+2:]):
                    continue

                s = sorted([num1, num2, remaining_number])
                if s[2] in found_sets.get(s[0], {}).get(s[1], {}):
                    continue
                else:
                    found_sets.setdefault(s[0], {})
                    found_sets[s[0]].setdefault(s[1], set())
                    found_sets[s[0]][s[1]].add(s[2])
                    combinations.append(s)

        return combinations