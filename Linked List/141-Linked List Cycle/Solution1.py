class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h_set = set()
        curr = head
        while curr:
            if curr not in h_set:
                h_set.add(curr)
            else:
                return True
            curr = curr.next
        return False
