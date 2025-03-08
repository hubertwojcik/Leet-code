class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        result = []

        def generate(opened_num, closed_num):
            if opened_num == closed_num == n:
                result.append("".join(stack))
                return
            if opened_num < n:
                stack.append("(")
                generate(opened_num + 1, closed_num)
                stack.pop()
            if closed_num < opened_num:
                stack.append(")")
                generate(opened_num, closed_num + 1)
                stack.pop()

        generate(0,0)
        return result