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

class Solution:
    def mergeTwoLists(self, a, b):
        if not a or b and a.val > b.val:
            a, b = b, a
        if a:
            a.next = self.mergeTwoLists(a.next, b)
        return a

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