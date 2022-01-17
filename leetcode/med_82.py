"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list. Return the linked list sorted as well.

E.g.1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

E.g.2:
Input: head = [1,1,1,2,3]
Output: [2,3]
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
        if not head or not head.next:
            return head
        pseudo_head = ListNode(val=-101, next=head)
        slow = pseudo_head
        fast = head
        val = None
        while fast.next:
            if fast.val != fast.next.val:
                slow.next = fast
                slow = slow.next
                fast = fast.next
                no_repeats = True
                continue
            val = fast.val
            while fast.next and (fast.val == val):
                fast = fast.next
                no_repeats = False
        if no_repeats or fast.val != val:
            slow.next = fast
        else:
            slow.next = None
        return pseudo_head.next

if __name__ == '__main__':
    
    head = [1,2,3,3,4,4,5]
    o = [1,2,5]
    
    head = [1,1,1,2,3]
    o = [2,3]
    
    head = [1,1]
    o = []
    
    head = construct_linkedlist(head)
    
    print(f'head: {head}')
    print(f'output: {o}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.deleteDuplicates(head))
    
    print(f'time duration: {time() - start}')


"""
Runtime: 91 ms, faster than 5.20% of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 14.2 MB, less than 58.80% of Python3 online submissions for Remove Duplicates from Sorted List II.
"""