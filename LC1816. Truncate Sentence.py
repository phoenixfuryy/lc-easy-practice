class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        new_s = " ".join(s.split()[0:k])
        return new_s