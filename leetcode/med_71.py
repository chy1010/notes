"""
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system,
convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory,
a double period '..' refers to the directory up a level,
and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'.

For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.

 
E.g.1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

E.g.2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.


E.g.3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        while '//' in path:
            path = path.replace('//', '/')
        
        path = path.lstrip("/").rstrip('/')
        structure = path.split('/')
        # print(structure)
        output_path = []
        for name in structure:
            if name == '..':
                if len(output_path) > 0:
                    output_path.pop()
                continue
            if name == '.':
                continue
            output_path.append(name)
        output_path = '/'.join(output_path)
        return '/'+output_path
            
        

if __name__ == '__main__':
    
    path = "/home//foo/"
    o = '/home/foo'
    
    path = "/../"
    o = "/"
    
    path = "/home/"
    o = "/home"
    
    print(f'path: {path}')
    print(f'o: {o}')
    print('-'*30)
    sol = Solution()
    from time import time
    start = time()
    
    print(sol.simplifyPath(path))
    
    
    print(f'time duration: {time() - start}')

"""
Runtime: 32 ms, faster than 78.38% of Python3 online submissions for Simplify Path.
Memory Usage: 14.4 MB, less than 45.82% of Python3 online submissions for Simplify Path.
"""