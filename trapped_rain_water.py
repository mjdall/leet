def trapped_rain_water(height):
    """
    Did bad time complexity version self.
    Watched 1/4 of a video, got some hints and then found solution.
    Based solution on product_except_self solution.
    :type height: List[int]
    :rtype: int
    """
    if not height or len(height) <= 2:
        return 0

    # create two lists that hold the
    # max height at index i on the left and right
    n = len(height)
    l_maxes = [height[0]]
    r_maxes = [height[-1]]
    lmax = height[0]
    rmax = height[-1]
    
    for i in range(1, n):
        # check if this spot has a higher spot than stored
        lmax = max(height[i], lmax)
        rmax = max(height[n-i-1], rmax)

        # append current maxes
        l_maxes.append(lmax)
        r_maxes.insert(0, rmax)

    total = 0
    for i in range(1, n-1):
        # get the current height, as well as the max height
        # on the left and right
        h = height[i]
        l = l_maxes[i-1]
        r = r_maxes[i+1]

        # find the min pillar height out of l and r
        max_in_spot = min(l, r)

        # calcualte the min pillar height dif with current height
        curr_dif = max_in_spot - h

        # if curr_dif > 0 then this spot can be filled with water
        # curr_dif now holds the amount of water we can fill this spot with
        if curr_dif > 0:
            total += curr_dif
            continue

    return total
