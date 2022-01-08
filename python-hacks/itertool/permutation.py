from itertools import permutations
import numpy as np

nums = [1,2,3]
perms = permutations(nums)
for num in perms:
    print(num)
    
nums = [1,1,2,13]
perms = permutations(nums)
for perm_nums in perms:
    print(perm_nums)