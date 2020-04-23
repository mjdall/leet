def spiral_order(self, matrix):
    """
    Returns the spiral order of the input matrix.
    I.e. [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    becomes [1, 2, 3, 6, 9, 8, 7, 4, 5].
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix or matrix is None:
        return []

    output = []

    # holds the limits for when we change axis direction
    curr_x_lim = len(matrix[0])
    curr_y_lim = len(matrix)

    # holds the total number of entries in the array
    #   as well as the number of total hops we need to do
    total_hops = curr_x_lim * curr_y_lim

    # the current directions we are travelling in the array
    # if x_direction is not 0 then y_direction will be 0, vice versa
    x_direction = 1
    y_direction = 0

    # the total number of steps we need to take in the current direction
    steps_in_direction = curr_x_lim
    
    # keep going until we've traversed each node
    x, y = 0, 0
    while total_hops != 0:
        # append the current spot in the matrix
        output.append(matrix[y][x])

        # increment variables keeping track of position
        steps_in_direction -= 1
        total_hops -= 1

        # we're done travelling in this direction
        if steps_in_direction == 0:
            # if we were travelling in x direction
            if x_direction:
                # y direction follows what x direction just was
                y_direction = x_direction

                # set x dir to zero
                x_direction = 0

                # the next time we traverse in x direction, we dont go as far
                curr_x_lim -= 1

                # set the number of steps we're expecting to take next
                steps_in_direction = curr_y_lim - 1
            else:
                # x direction changes direction to y
                x_direction = -y_direction

                y_direction = 0
                curr_y_lim -= 1
                steps_in_direction = curr_x_lim

        # get the next spot in the array
        x += x_direction
        y += y_direction

    return output
      