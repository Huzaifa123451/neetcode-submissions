# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        elif head.next is None:
            return False
        else:
            seen = set()
            while head is not None:
                seen.add(head)
                if head.next in seen:
                    return True
                head = head.next
            return False