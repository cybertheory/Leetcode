# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = []
        res = None
        while head:
            nodes.append(head.val)
            head = head.next
        while nodes:
            res=ListNode(nodes.pop(0),res)
        return res
        