"""
Knuth-Morris-Pratt algorithm
https://leetcode.com/problems/implement-strstr/discuss/119566/Python-KnuthMorrisPratt-algorithm

refer: https://zh.wikipedia.org/wiki/KMP%E7%AE%97%E6%B3%95
"""
from collections import Counter
class Solution:
    def build_lps(self, pattern):
        """ Helper function for strStr.
        Returns longest proper suffix array for string pattern.
        Each lps_array[i] is the length of the longest proper prefix
        which is equal to suffix for pattern ending at character i.
        Proper means that whole string cannot be prefix or suffix.

        Time complexity: O(m). Space complexity: O(1), where
        m is the length of the pattern, space used for lps array isn't included.
        """
        m = len(pattern)
        lps_array = [0] * m
        i, j = 1, 0  # start from the 2nd character in pattern
        while i < m:
            if pattern[i] == pattern[j]:
                lps_array[i] = j + 1
                j += 1
                i += 1
            else:
                if j > 0:
                    j = lps_array[j - 1]
                else:
                    lps_array[i] = 0
                    i += 1
        return lps_array

    def strStr(self, text, pattern):
        """ Returns index of 1st occurence of pattern in text.
        Returns -1 if pattern is not in the text.
        Knuth-Morris-Pratt algorithm.
        Time complexity: O(n + m). Space complexity: O(m).
        """
        # special cases
        if not text and not pattern:
            return 0
        elif not pattern:
            return 0

        # build longest proper suffix array for pattern
        lps_array = self.build_lps(pattern)
        # counter = Counter(lps_array)
        # print(counter)

        n, m = len(text), len(pattern)
        i, j = 0, 0
        while i < n:
            # current characters match, move to the next characters
            if text[i] == pattern[j]:
                i += 1
                j += 1
            # current characters don't match
            else:
                if j > 0:  # try start with previous longest prefix
                    j = lps_array[j - 1]
                # 1st character of pattern doesn't match character in text
                # go to the next character in text
                else:
                    i += 1

            # whole pattern matches text, match is found
            if j == m:
                return i - m

        # no match was found
        return -1

    
    
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
    
    # with open('temp/easy_28_test_case2.txt', mode='r') as fp:
    #     inputs = fp.read().splitlines()
    # haystack = inputs[0].strip('"')
    # needle = inputs[1].strip('"')
    # expected = -1
    
    # from collections import Counter
    # counter1 = Counter(haystack)
    # counter2 = Counter(needle)
    # print(counter1)
    # print(counter2)
    
    haystack = "mississippi"
    needle = "mississippii"
    
    # haystack = "mississippi"
    # needle = "issi"
    
    # haystack = "bbbbababbbaabbba"
    # needle = "abb"
    
    print(f'haystack: {haystack}')
    print(f'needle: {needle}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.strStr(haystack, needle))
    
    print(f'time duration: {time() - start}')