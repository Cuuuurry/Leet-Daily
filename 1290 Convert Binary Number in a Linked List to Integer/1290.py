# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        while head:
            result = result * 2 + head.val
            head = head.next

        return result