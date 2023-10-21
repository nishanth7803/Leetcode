class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        zero, ans = 0, 0
        while r < len(nums):
            if nums[r] == 0:
                zero += 1
            while zero > k:
                if nums[l] == 0:
                    zero -= 1
                l += 1
            ans = max(ans, r-l+1)
            r += 1
        return ans
