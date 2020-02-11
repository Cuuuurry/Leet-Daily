class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        if head.val == head.next.val:
            head.next = head.next.next
            head = self.deleteDuplicates(head)
        else:
            head.next = self.deleteDuplicates(head.next)

        return head