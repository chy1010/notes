def build_lps(pattern):
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
    
    
if __name__ == '__main__':
    #          0123456789ABCD
    pattern = 'abcdeeeabcabdd'
    
    # at position 789: match the prefix 012
    # at position AB: match the prefix 01
    
    # use this information, when matching at i fails,
    # the next match should begin at i+7
    
    print(build_lps(pattern))
    
    
    # import random
    # char_list = ['a', 'b', 'c', 'd']
    # text = [ random.choice(char_list) for _ in range(40)]
    # text = ''.join(text)
    # pattern = 'abcdabcabdab'
    #          01234567890123456789012345678
    text    = 'ABCFABCDABEABCDABDAFABCDABDAB'
    pattern = 'ABCDABDAB'
    #          012345678
    
    print(f'text: {text}')
    print(f'pattern: {pattern}')
    print(f'lps: {build_lps(pattern)}')
    m = len(text)
    n = len(pattern)
    i, j = 0, 0
    lps_array = build_lps(pattern)
    import ipdb
    ipdb.set_trace()
    while i < m:
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
            print(f'matched at {i-m}!')
            break
    print('not matched!')