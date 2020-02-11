# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dif = 1
        firstNode = head
        secondeNode = head
        while firstNode.next:
            firstNode = firstNode.next
            if dif > n:
                secondeNode = secondeNode.next
            dif += 1
        if dif == n:
            return head.next
        secondeNode.next = secondeNode.next.next
        return head