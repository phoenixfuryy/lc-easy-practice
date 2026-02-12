class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums

        """for i, el in enumerate(nums):
            if i>=1:
                nums[i] = nums[i]+nums[i-1]
            print(nums)"""
    
""" 
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
   
"""
