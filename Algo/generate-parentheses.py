"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


class Solution:

    def generateParenthesis(self, n):
        ps = []
        if(n > 0):
            ls = [""]*2*n
            alocate(ps, ls, 0, n, 0, 0)
        return ps


def alocate(ps, ls, pos, n, op, cp):
    if(cp == n):
        rs = []
        for i in ls:
            rs.append(i)
        ps.append("".join(rs))
    else:
        if(op > cp):
            ls[pos] = ')'
            alocate(ps, ls, pos + 1, n, op, cp + 1)
        if(op < n):
            ls[pos] = '('
            alocate(ps, ls, pos + 1, n, op + 1, cp)


n = 3
sol = Solution()
rs = sol.generateParenthesis(n)
print(rs)
