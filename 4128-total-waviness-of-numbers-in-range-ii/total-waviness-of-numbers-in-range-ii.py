class Solution(object):
    def totalWaviness(self, num1, num2):
        def solve(n):
            s = str(n)
            memo = {}
            def dp(i, tight, a, b):
                if i == len(s):
                    return (0, 1)
                key = (i, tight, a, b)
                if key in memo:
                    return memo[key]
                ways = total = 0
                for d in range(10 if not tight else int(s[i]) + 1):
                    nt = tight and d == int(s[i])
                    if a == -1 and d == 0:
                        x, y = dp(i+1, nt, -1, -1)
                        add = 0
                    elif a == -1:
                        x, y = dp(i+1, nt, d, -1)
                        add = 0
                    elif b == -1:
                        x, y = dp(i+1, nt, a, d)
                        add = 0
                    else:
                        add = int((b>a and b>d) or (b<a and b<d))
                        x, y = dp(i+1, nt, b, d)
                    ways += x + y * add
                    total += y
                memo[key] = (ways, total)
                return memo[key]
            return dp(0, True, -1, -1)[0]
        return solve(num2) - solve(num1-1)
