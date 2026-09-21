# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr is not None:
            temp = curr.next # save next value
            curr.next = prev #that value becomes the previous val
            prev = curr #prev val pointer points to  that next val
            curr = temp #now we do the same for that next val
        return prev
       