class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits_list = [int(d) for d in str(n)]
        product, sum, result  = 1, 0, 0
        for i, el in enumerate(digits_list):
            product = product * el
            sum = sum + el
        result = product - sum
        return result

        


 """for i in range(len(digits_list)):
            product = product * digits_list[i]
            print(product)"""