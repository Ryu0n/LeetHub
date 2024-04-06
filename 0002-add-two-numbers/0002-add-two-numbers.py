# Definition for singly-linked list.
class ListNode(object):
    CRITERION = 9
    def __init__(self, val=0, next=None):
        self._val = val
        self.next = next
    
    @property
    def val(self):
        return self._val
    
    @val.setter
    def val(self, val):
        d10, d1 = divmod(val, self.CRITERION+1)
        self._val = d1
        if d10 > 0:
            if self.next is not None:
                self.next.val += d10
            else:
                self.next = ListNode(d10)

    @classmethod
    def reinitialize(cls, ln):
        cn = ListNode(val=ln.val)
        if ln.next is None:
            return cn
        nn = cls.reinitialize(ln.next)
        cn.next = nn
        return cn

    def propagate(self, ln):
        self.val += ln.val
        if self.next is not None:
            nln = ln.next if ln.next is not None else ListNode()
            self.next.propagate(nln)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = ListNode.reinitialize(l1)
        l2 = ListNode.reinitialize(l2)
        l1.propagate(l2)
        return l1
