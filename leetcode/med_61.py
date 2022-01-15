"""
Given the head of a linked list, rotate the list to the right by k places.

E.g.1:
head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

E.g.2:
head = [0,1,2], k = 4
Output: [2,0,1]
"""
from typing import Optional
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
    node = None
    for val in nodelist[::-1]:
        node = ListNode(val, previous_node)
        previous_node = node
    return node
    
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        if k == 0:
            return head
        slow = head
        fast = head
        i = 0
        while i < k:
            if not fast.next:
                return self.rotateRight(head, k % (i+1))
            fast = fast.next
            i += 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = head
        head = slow.next
        slow.next = None
        return head
    

if __name__ == '__main__':
    
    head = [1,2,3,4,5]
    k = 2
    expected = [4,5,1,2,3]
    
    head = []
    k = 1
    
    print(f'head: {head}, k: {k}')
    print(f'expected: {expected}')
    print('-'*30)
    
    head = construct_linkedlist(head)
    
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.rotateRight(head, k))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 59 ms, faster than 17.42% of Python3 online submissions for Rotate List.
Memory Usage: 14.2 MB, less than 60.15% of Python3 online submissions for Rotate List.
"""