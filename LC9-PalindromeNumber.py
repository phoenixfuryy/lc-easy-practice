class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        """if (x>=0):
            xlist = [int(d) for d in str(x)]
            reversed_xlist = list(reversed(xlist))
            if (xlist == reversed_xlist):
                return True
            else: 
                return False 
        else:
            return False"""
        
        if(x<0):
            return False
        if (x>=0):
            xlist = [int(d) for d in str(x)]
            leftP, rightP = 0, len(xlist)-1
            for i in range(len(xlist)):
                while(leftP < rightP):
                    if xlist[leftP] == xlist[rightP]:
                        leftP+=1
                        rightP-=1
                    else:
                        return False
                return True
            

