import bisect
class Solution():
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.__getitem__ = isBadVersion
        return bisect.bisect_left(self, True, 1, n)