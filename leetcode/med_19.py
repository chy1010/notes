"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

E.g.1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

E.g.2:
Input: head = [1], n = 1
Output: []

E.g.3:
Input: head = [1,2], n = 1
Output: [1]
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
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        i = 0
        while i < n:
            node = node.next
            i+=1
        cut_node = None
        while True:
            if node is None:
                if cut_node is None:
                    return head.next
                else:
                    cut_node.next = cut_node.next.next
                    break
            node = node.next
            cut_node = cut_node.next if cut_node is not None else head
            
        return head

if __name__ == '__main__':
    
    head = [1,2]
    n = 1
    expected = [1]
    
    head = [1]
    n = 1
    expected = []

    head = [1,2,3,4,5]
    n = 2
    expected = [1,2,3,5]
    
    previous_node = None
    for val in head[::-1]:
        node = ListNode(val, previous_node)
        previous_node = node
    
    head = node
    from time import time
    sol = Solution()
    start = time()
    result = sol.removeNthFromEnd(head, n)
    print(f'time duration: {time() - start}')
    
    if result is None:
        print('result: []')
    else:
        print('result:', list(result))
    
    
"""
Runtime: 32 ms, faster than 77.79% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14.4 MB, less than 14.39% of Python3 online submissions for Remove Nth Node From End of List.
"""