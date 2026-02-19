class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        """
        Time complexity is O(n²)
        output = []
        for i in range(len(arr)):
            if i == len(arr)-1:
                output.append(-1)
            else:
                output.append(max(arr[i+1:]))
        return output
        """
        rightMax = -1
        for i in range(len(arr)-1, -1, -1):
            newMax = max(arr[i],rightMax)
            arr[i] = rightMax
            rightMax = newMax
        return arr