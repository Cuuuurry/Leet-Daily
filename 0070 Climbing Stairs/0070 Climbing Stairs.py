class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            step_methods = [1, 2, 0]
            for i in range(2, n):
                step_methods[-1] = step_methods[0] + step_methods[1]
                step_methods[0] = step_methods[1]
                step_methods[1] = step_methods[-1]
            return step_methods[-1]
