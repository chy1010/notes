"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list.
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            if list1.val <= list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2

if __name__ == '__main__':
    
    
    list1 = [1,2,4]
    list2 = [1,3,4]
    expected = [1,1,2,3,4,4]
    
    # list1 = []
    # list2 = []
    # expected = '[]'
    
    list1 = construct_linkedlist(list1)
    list2 = construct_linkedlist(list2)
    
    print(f'list1: {list1}')
    print(f'list2: {list2}')
    print(f'expected: {expected}')
    print('-'*30)
    
    import tracemalloc
    tracemalloc.start()  
    sol = Solution()
    from time import time
    start = time()
    print(sol.mergeTwoLists(list1, list2))
    print(f'time duration: {time() - start}')
    current, peak = tracemalloc.get_traced_memory() 
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")  
    tracemalloc.stop()



"""
Runtime: 42 ms, faster than 22.80% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.2 MB, less than 62.75% of Python3 online submissions for Merge Two Sorted Lists.
--
Runtime: 53 ms, faster than 13.92% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.3 MB, less than 62.75% of Python3 online submissions for Merge Two Sorted Lists.
--
Runtime: 45 ms, faster than 18.93% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.4 MB, less than 31.63% of Python3 online submissions for Merge Two Sorted Lists.
"""    