#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        else:
            nodes = [head]
            while head.next is not None:
                head = head.next
                nodes.append(head)

        virtualHead = ListNode(-1)
        head = virtualHead

        while nodes:
            head.next = nodes.pop()
            head = head.next
        head.next = None
        return virtualHead.next

# @lc code=end

