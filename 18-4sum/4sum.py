class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                l, r = j+1, n-1
                while l < r:
                    s = nums[i]+nums[j]+nums[l]+nums[r]
                    if s == target:
                        x = [nums[i],nums[j],nums[l],nums[r]]
                        if x not in ans: ans.append(x)
                        l += 1
                        r -= 1
                    elif s < target: l += 1
                    else: r -= 1
        return ans

        