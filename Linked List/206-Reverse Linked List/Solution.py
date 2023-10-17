class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev