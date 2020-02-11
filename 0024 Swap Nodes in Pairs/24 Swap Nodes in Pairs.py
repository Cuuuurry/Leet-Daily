# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        second = head.next
        first = head
        third = second.next
        second.next = first

        def nextPart(preNode, headOfRest):
            if not headOfRest or not headOfRest.next:
                return headOfRest

            second = headOfRest.next
            nextHeadOfRest = second.next
            preNode.next = second
            second.next = headOfRest
            headOfRest.next = nextPart(headOfRest, nextHeadOfRest)

            return second

        first.next = nextPart(first, third)

        return second