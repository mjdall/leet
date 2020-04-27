def reverse(x):
    """
    Reverses an integer.
    I.e. 123 becomes 321, -123 becomes -321
        123000 becomes 321.
    :type x: int
    :rtype: int
    """

    # need to reverse a positive number
    # this keeps track of initial sign
    mult = 1 if x > 0 else -1

    # make x postive
    x *= mult

    # the var to store final x in
    reversed_num = 0

    # while x isnt 0
    while x:
        # shift the current reversed number by 1
        reversed_num *= 10

        # add the current number
        reversed_num += x % 10

        # shift the last added digit from x off
        x //= 10

    # add the initial sign back in and return
    reversed_num *= mult
    return reversed_num
