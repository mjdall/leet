def trapped_rain_water(height):
        """
        Did self, needs time complexity work.
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) <= 2:
            return 0

        # total amount of rain we've collected
        total = 0
        i = 1

        while i < len(height)-1:
            prev = height[i-1]
            curr = height[i]
            nxt = height[i+1]
            
            if prev <= curr:
                i += 1
                continue
            
            for h2 in height[i+1:]:
                if h2 > curr:
                    break
            else:
                i += 1
                continue
            
            height[i] += 1
            total += 1

        return total
