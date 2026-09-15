class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self._left = ListNode(0)
        self._right = ListNode(0)
        self._left.next = self._right
        self._right.prev = self._left

    def get(self, index: int) -> int:
        curr = self._left.next
        while curr is not None and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self._right and index == 0:
            return curr.val

        return -1


    def addAtHead(self, val: int) -> None:
        newNode, next, prev = ListNode(val), self._left.next, self._left
        prev.next = newNode
        next.prev = newNode
        newNode.next = next
        newNode.prev = prev

    def addAtTail(self, val: int) -> None:
        node, next, prev = ListNode(val), self._right, self._right.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self._left.next
        while curr is not None and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            newNode, next, prev = ListNode(val), curr, curr.prev
            prev.next = newNode
            next.prev = newNode
            newNode.next = next
            newNode.prev = prev

    def deleteAtIndex(self, index: int) -> None:
        curr = self._left.next
        while curr is not None and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self._right and index == 0:
            next, prev = curr.next, curr.prev
            next.prev = prev
            prev.next = next
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)