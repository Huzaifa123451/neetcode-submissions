# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        curr = head

        while n > 0:
            curr = curr.next
            n -= 1 #iterate all the way until we have reached nth node
        while curr:
            left = left.next
            curr = curr.next
        # n -1th node points to n+1th node now
        left.next = left.next.next
        return dummy.next
