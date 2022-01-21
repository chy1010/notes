"""
Given the head of a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

E.g.1
head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

E.g.2
head = [2,1], x = 2
Output: [1,2]
"""

from typing import Optional
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        small = pseudo_small_head = ListNode(val=-101)
        larger = pseudo_larger_head = ListNode(val=-101)
        p = head
        while p:
            if p.val >= x:
                larger.next = p
                larger = larger.next
            else:
                small.next = p
                small = small.next
            p = p.next
        small.next = pseudo_larger_head.next
        larger.next = None
        return pseudo_small_head.next
        
        

if __name__ == '__main__':
    
    head = [1,4,3,2,5,2]
    x = 3
    o = [1,2,2,4,3,5]
    
    head = [2,1]
    x = 2
    o = [1,2]
    
    head = construct_linkedlist(head)
    
    print(f'head: {head}')
    print(f'o: {o}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.partition(head, x))
    
    print(f'time duration: {time() - start}')

"""
Runtime: 24 ms, faster than 99.41% of Python3 online submissions for Partition List.
Memory Usage: 14.4 MB, less than 29.22% of Python3 online submissions for Partition List.
"""