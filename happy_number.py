def iterate_digits(num):
    while num:
        curr_digit = num % 10
        num //= 10
        print(curr_digit)

def is_happy(n, seen=set()):
        """
        todo: explain happy number
        :type n: int
        :rtype: bool
        """
        sq_sum = 0
        while n:
            sq_sum += (n % 10)**2
            print(n, sq_sum)
            n //= 10

        if sq_sum == 1:
            return True
        if sq_sum in seen:
            return False
        seen.add(sq_sum)

        return is_happy(sq_sum, seen)
