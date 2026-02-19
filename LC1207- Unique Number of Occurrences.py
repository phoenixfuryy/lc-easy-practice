from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = Counter(arr)
        arr_dict = dict(count)
        if(len(arr_dict.values()) == len(set(arr_dict.values()))):
            return True
        else:
            return False