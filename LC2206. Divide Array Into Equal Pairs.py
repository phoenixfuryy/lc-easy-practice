from collections import Counter
class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = Counter(nums)
        print(count)
        print(type(count))
        print(count.values())
        for el in count.values():
            if(el%2 == 0):
                print("true")
            else:
                print("false")
        

s1 = Solution()
s1.divideArray([1,2,2,4])