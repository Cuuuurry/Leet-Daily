# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodeList = []

        def nextNode(node, nodeList):
            if node:
                nodeList.append(node)
                nextNode(node.next, nodeList)
            else:
                return

        nextNode(head, nodeList)
        if n == len(nodeList):
            return head.next
        if n == 1:
            nodeList[-2].next = None
            return head
        before = nodeList[-n - 1]
        after = nodeList[-n + 1]

        before.next = after
        return head
    