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
        temp = head
        head = None
        while temp:
            head = ListNode(temp.val, head )
            temp = temp.next
        return head
            