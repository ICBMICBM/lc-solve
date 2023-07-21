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
            vals = [head.val]
            while head.next:
                head = head.next
                vals.append(head.val)

        virtualHead = ListNode(-1)
        head = virtualHead
        # print(vals)
        while vals:
            newNode = ListNode(vals.pop())
            head.next = newNode
            head = newNode
        return virtualHead.next

# @lc code=end

