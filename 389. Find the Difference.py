class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        """
        TC: O(n^2)
        s_list = list(s)
        t_list = list(t)
        for el in t_list:
            if el not in s_list:
                return el
            else:
                s_list.pop(s_list.index(el))
        """   

        s_sum, t_sum = 0, 0
        for ch in s:
            s_sum += ord(ch)
        for ch in t:
            t_sum += ord(ch)
        diff = t_sum - s_sum
        return chr(diff)
             
        