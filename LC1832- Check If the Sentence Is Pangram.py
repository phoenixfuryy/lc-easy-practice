class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        set1 = set()
        for i, el in enumerate(sentence):
            set1.add(el)
        if len(set1) == 26: 
            return True
        else: 
            return False
        