"""
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)

E.g.1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

E.g.2:
Input: head = []
Output: []

E.g.3:
Input: head = [1]
Output: [1]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __iter__(self):
        val_list = [self.val]
        node = self.next
        while node is not None:
            val_list.append(node.val)
            node = node.next
        for val in val_list:
            yield val
            
    def __repr__(self):
        return f'{list(self)}'

def construct_linkedlist(nodelist):
    """[summary]
    Args:
        nodelist: list of values of node
    Returns:
        ListNode: head of the linkedlist.
    """    
    previous_node = None
    for val in nodelist[::-1]:
        node = ListNode(val, previous_node)
        previous_node = node
    return previous_node

from typing import Optional
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        new_head = head.next
        tail = self.swapPairs(new_head.next)
        new_head.next = head
        head.next = tail
        return new_head

if __name__ == '__main__':
    
    head = [1,2,3,4]
    
    # head = []
    
    # head = [1]
    
    head = construct_linkedlist(head)
    
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.swapPairs(head))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 56 ms, faster than 5.43% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 14.3 MB, less than 50.10% of Python3 online submissions for Swap Nodes in Pairs.
"""