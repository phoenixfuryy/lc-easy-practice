class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = "".join(map(str, digits))
        newVal = int(s) + 1
        return [int(d) for d in str(newVal)]