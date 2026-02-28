from collections import Counter
class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        num_dict = {i : int(d) for i, d in enumerate(num)}
        print(num_dict)
        count = 0
        for i in range(len(num)-1):
            if i in int(list(num)):
                print(i)
                print("test1")
                count += 1
                print(count)
        
s1 = Solution()
s1.digitCount("1210")