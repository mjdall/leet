def removeKdigits(self, num, k):
    """
    Returns the minimum number after removing any k
        numbers from input num.
    :type num: str
    :type k: int
    :rtype: str
    """
    if len(num) == k:
        return "0"
    
    num_list = []
    self.backtrack(num_list, num, k)
    
    # return the num as a string
    return(str(min(num_list)))
        
def backtrack(self, num_list, num, k):
    # removed all the digits we need to, so append
    if k == 0:
        num_list.append(int(num))
        return()
    
    # call backtrack after removing each digit
    for i in range(0, len(num)-1):
        n = str(num)
        n = n[:i] + n[i+1:]
        
        self.backtrack(num_list, n, k-1)
    
    # backtrack with removing the last digit
    self.backtrack(num_list, num[:-1], k-1)