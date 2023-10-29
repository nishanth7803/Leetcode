class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h_map = {0:1}
        currsum,ans = 0,0
        for i in nums:
            currsum+=i
            if currsum-k in h_map:
                ans+=h_map[currsum-k]
            h_map[currsum] = h_map.get(currsum, 0) + 1
        return ans
