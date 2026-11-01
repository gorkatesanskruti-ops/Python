class Solution(object):
    def letterCombinations(self, digits):
        #sets 
        #cartesion product 
        phone = {'2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'}
        ans = [""]
        for d in digits:
            temp = []
            for x in ans:
                for ch in phone[d]:
                    temp.append(x + ch)
            ans = temp
        return ans
