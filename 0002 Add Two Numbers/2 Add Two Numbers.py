# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            num1 = l1.val
            move = num1 // 10
            res = num1 % 10
            l1.val = res
            if not move:
                pass
            elif not l1.next:
                l1.next = ListNode(move)
            else:
                l1.next.val += move

            nextNum = self.addTwoNumbers(l1.next, None)
            return l1

        num1 = l1.val
        num2 = l2.val
        move = (num1 + num2) // 10
        res = (num1 + num2) % 10
        ans = ListNode(res)
        if not move:
            pass
        elif not l1.next:
            l1.next = ListNode(move)
        else:
            l1.next.val += move

        nextNum = self.addTwoNumbers(l1.next, l2.next)
        ans.next = nextNum

        return ans