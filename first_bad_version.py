def firstBadVersion(self, n):
    """
    Suppose you have n versions [1, 2, ..., n],
         you want to find out the first bad one, which causes all the following ones to be bad.

    You are given an API bool isBadVersion(version) which will return whether version is bad.
    Implement a function to find the first bad version.
    You should minimize the number of calls to the API.
    :type n: int
    :rtype: int
    """

    if isBadVersion(1):
        return 1
    
    check_version = n // 2
    last_good_version = 1
    last_bad_version = n
    
    while last_good_version + 1 != last_bad_version:
        if isBadVersion(check_version):
            last_bad_version = check_version
        else:
            last_good_version = check_version
        
        check_version = (last_bad_version + last_good_version) // 2
    
    return last_bad_version
