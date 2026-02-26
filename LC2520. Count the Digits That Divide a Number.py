class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        digits_list = [int(d) for d in str(num)]
        for el in digits_list:
            if num % el == 0:
                count+=1
        return count