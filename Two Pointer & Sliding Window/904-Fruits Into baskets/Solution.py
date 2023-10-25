class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        h_map = {}
        l, ans = 0, 0
        for r in range(len(fruits)):
            h_map[fruits[r]] = h_map.get(fruits[r], 0) + 1
            while len(h_map) > 2:
                h_map[fruits[l]] -= 1
                if h_map[fruits[l]] == 0:
                    del h_map[fruits[l]]
                l += 1
            ans = max(ans, r-l+1)
        return ans
