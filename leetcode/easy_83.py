"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

E.g.1
Input: head = [1,1,2]
Output: [1,2]

E.g.2
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""
from typing import List, Optional
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
    return node

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        slow = fast = head
        while fast.next:
            fast = fast.next
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
        slow.next = None
        return head

if __name__ == '__main__':
    
    head = [1,1,2,3,3]
    o = [1,2,3]
    
    head = [1,1,2]
    o = [1,2]
    
    head = construct_linkedlist(head)
    
    print(f'head: {head}')
    print(f'o: {o}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.deleteDuplicates(head))
    
    print(f'time duration: {time() - start}')


"""
Runtime: 60 ms, faster than 28.52% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 14.2 MB, less than 82.63% of Python3 online submissions for Remove Duplicates from Sorted List.
"""