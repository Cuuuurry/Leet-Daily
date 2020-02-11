class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        node = head
        count = 0
        while node:
            lastNode = node
            node = node.next
            count += 1

        lastNode.next = head
        beginNode = head
        beginNum = (count - k ) %count

        for i in range(beginNum):
            lastNode = beginNode
            beginNode = beginNode.next
        lastNode.next = None

        return beginNode
