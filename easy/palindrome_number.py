from math import floor, log10

def is_palindrome(self, x):
        """
        Determins if a number is a palindrome without converting to a string.
        :type x: int
        :rtype: bool
        """
        # negative numbers cant be palindromes
        if x < 0:
            return False

        # loop until we have 0 (equal len number) or 1-9 (odd len number)
        while x > 10:
            # get the msd and lsd's
            largest_digit =  int(x / pow(10, floor(log10(x))))
            smallest_digit = x % 10
            
            # if they dont match the number isnt a palindrome
            if largest_digit != smallest_digit:
                return False
            
            # remove msd
            x = int(x % pow(10, floor(log10(x))))
         
            # remove lsd
            x /= 10
        
        # breaking means number is a palindrome
        return True