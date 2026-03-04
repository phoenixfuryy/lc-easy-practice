from collections import Counter
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        good_pairs_count = 0
        count = Counter(nums)
        print(count)
        for el in nums: 
            count[el] -= 1
            good_pairs_count += count[el]
        print(good_pairs_count)         
s1 = Solution()
s1.numIdenticalPairs([1,1,1,1])