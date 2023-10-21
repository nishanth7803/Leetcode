class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans, currsum = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                currsum += 1
                if i == len(nums)-1:
                    ans = max(ans, currsum)
            else:
                ans = max(ans, currsum)
                currsum = 0
        return ans
