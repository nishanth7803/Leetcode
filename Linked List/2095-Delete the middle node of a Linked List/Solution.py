# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        x = dummy
        slow, fast = head, head
        y = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            x = x.next
        x.next = slow.next
        return dummy.next
