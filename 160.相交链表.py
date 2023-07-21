#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def makeDump(self, n: ListNode):
        dump = {}
        ids = []
        dump[id(n)] = n
        ids.append(id(n))
        while n.next is not None:
            n = n.next
            dump[id(n)] = n
            ids.append(id(n))
        return dump, ids
    
    def intersection(self, l1, l2):
        l1 = set(l1)
        for i in l2:
            if i in l1:
                return i
        return None


    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dumpA, idA = self.makeDump(headA)
        _, idB = self.makeDump(headB)
        duplicate = self.intersection(idA, idB)
        if duplicate is None:
            return None
        else:
            return dumpA[duplicate]
        
        
# @lc code=end

