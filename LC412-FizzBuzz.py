class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arrayList = []
        i=1
        while i<=n:
            if(i%3==0 and i%5==0):
                arrayList.append("FizzBuzz")
            elif(i%3==0):
                arrayList.append("Fizz")
            elif(i%5==0):
                arrayList.append("Buzz")
            else:
                arrayList.append(str(i))
            i+=1
        return arrayList
                