# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2, d10=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None if d10 == 0 else ListNode(val=d10, next=None)
        v1 = l1.val if l1 is not None else 0
        v2 = l2.val if l2 is not None else 0
        s = (v1 + v2) + d10
        d10, d1 = s // 10, s % 10
        n1 = l1.next if l1 is not None else None
        n2 = l2.next if l2 is not None else None
        ln = self.addTwoNumbers(n1, n2, d10)
        return ListNode(val=d1, next=ln)
