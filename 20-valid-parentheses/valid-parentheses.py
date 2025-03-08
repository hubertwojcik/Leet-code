class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        close_to_open = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for c in s:
            if c in close_to_open:
                if stack and close_to_open[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        