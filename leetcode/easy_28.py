"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""
from collections import defaultdict
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        
        # start = time()
        needle_table = defaultdict(list)
        for ind, char in enumerate(needle):
            needle_table[char].append(ind)
        
        haystack_table = defaultdict(list)
        for ind, char in enumerate(haystack):
            haystack_table[char].append(ind)

        matching_procedures = iter(sorted(needle_table.items(), key=lambda letter_positions: len(letter_positions[1])))
        shortest, needle_positions = next(matching_procedures)
        if shortest not in haystack_table:
            return -1
        hay_positions = haystack_table[shortest]
        n = len(hay_positions)
        m = len(needle_positions)
        if m > n:
            return -1
        
        possible_shifts = []
        
        for j in range(n-m+1):
            i = 0
            shift = hay_positions[j] - needle_positions[0]
            matched = True
            while i < m:
                if (hay_positions[j+i] - needle_positions[i]) != shift:
                    matched = False
                    break
                i+=1
            if matched:
                possible_shifts.append(shift)
        
        try:
            while True:
                possible_shifts_here = []
                c, needle_positions = next(matching_procedures)
                if c not in haystack_table:
                    return -1
                hay_positions = haystack_table[c]
                n = len(hay_positions)
                m = len(needle_positions)
                if m > n:
                    return -1
                for j in range(n-m+1):
                    i = 0
                    shift = hay_positions[j] - needle_positions[0]
                    if shift not in possible_shifts:
                        continue
                    matched = True
                    while i < m:
                        if (hay_positions[j+i] - needle_positions[i]) != shift:
                            matched = False
                            break
                        i+=1
                    if matched:
                        possible_shifts_here.append(shift)
                possible_shifts = list(set(possible_shifts).intersection(set(possible_shifts_here)))
                
        except StopIteration:
            pass
                
        return sorted(possible_shifts)[0] if possible_shifts else -1
    

if __name__ == '__main__':
    
    haystack = "hellohhhhhhheeeeeeooooppppppppll"
    needle = "ll"
    expected =  2
    
    # haystack = "aaaaa"
    # needle = "bba"
    # expected = -1
    
    # haystack = "aaa"
    # needle = "aaaa"
    # expected = -1
    
    with open('temp/easy_28_test_case2.txt', mode='r') as fp:
        inputs = fp.read().splitlines()
    haystack = inputs[0].strip('"')
    needle = inputs[1].strip('"')
    expected = -1
    
    from collections import Counter
    counter1 = Counter(haystack)
    counter2 = Counter(needle)
    print(counter1)
    print(counter2)
    
    # haystack = "mississippi"
    # needle = "mississippii"
    
    # haystack = "mississippi"
    # needle = "issi"
    
    # haystack = "bbbbababbbaabbba"
    # needle = "abb"
    
    # print(f'haystack: {haystack}')
    # print(f'needle: {needle}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.strStr(haystack=haystack, needle=needle))
    
    print(f'time duration: {time() - start}')
    
"""
Runtime: 83 ms, faster than 19.01% of Python3 online submissions for Implement strStr().
Memory Usage: 17.1 MB, less than 5.49% of Python3 online submissions for Implement strStr().
"""