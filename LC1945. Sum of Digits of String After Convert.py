class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result = "".join((str(ord(ch)-96))for ch in s)
        i = 0
        while(i!=k):
            total = sum(int(d) for d in result)
            result = str(total)
            i+=1
        return total