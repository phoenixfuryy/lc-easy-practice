class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftP = 0
        rightP = len(nums)-1
        for el in nums:
            if (nums[leftP] % 2 != 0):
                if nums[rightP] %2 == 0:
                    nums[leftP], nums[rightP] = nums[rightP], nums[leftP]
                    leftP+=1
                else:
                    rightP -=1
            else:
                leftP+=1
        return nums



        