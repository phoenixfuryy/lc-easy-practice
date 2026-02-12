class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i=2
        count = 1
        divisorsArray = []
        while(i*i<=num and num!=1):
            if(num%i==0 and i!=num and num!=1):
                divisor = num/i
                if divisor not in divisorsArray: 
                    divisorsArray.append(divisor)
                    count = count + divisor + i
            i += 1
        
        if num!= 1 and count == num:
            return True
        else:
            return False
        