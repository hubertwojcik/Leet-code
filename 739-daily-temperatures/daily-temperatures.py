class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_t, stack_idx = stack.pop()
                result[stack_idx] = (i - stack_idx)
            stack.append([t, i])
        return result
        