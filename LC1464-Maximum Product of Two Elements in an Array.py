class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        
        print((sorted_nums[len(sorted_nums)-1]-1) * (sorted_nums[len(sorted_nums)-2]-1))
s1 = Solution()
s1.maxProduct([3,4,5,2])