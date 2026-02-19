class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        replacements = {
            '()':'o',
            '(al)': 'al'
        }
        for old, new in replacements.items():
            command = command.replace(old, new)
        return command