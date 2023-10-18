class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left, right = 0,k-1
        ans = currsum = 0
        for i in range(left, right+1):
            currsum += arr[i]
        right = right+1
        if currsum/k >= threshold:
            ans += 1
        while right < len(arr):
            currsum += arr[right]
            currsum -= arr[left]
            left += 1
            right += 1
            if currsum/k >= threshold:
                ans += 1
        return ans
