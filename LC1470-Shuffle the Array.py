class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        output = []
        for i in range(len(nums)/2):
            p1 = nums[i]
            p2 = nums[n+i]
            output.append(p1)
            output.append(p2)
        return output