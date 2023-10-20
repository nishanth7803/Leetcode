class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0, 0
        currsum = nums[l]
        ans = float('inf')
        check = False
        while r<len(nums) and l<=r:
            if currsum >= target:
                check = True
                ans = min(ans, r-l+1)
                currsum -= nums[l]
                l += 1
            elif currsum < target:
                r += 1
                if r == len(nums):
                    break
                currsum += nums[r]
        if check:
            return ans
        return 0
