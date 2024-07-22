class Solution:
    def simplifyPath(self, s: str) -> str:
        stk,curr = [],""
        for i in s+'/':
            if i == '/':
                if curr == '..':
                    if stk:
                        stk.pop()
                elif curr != '.' and curr != '':
                    stk.append(curr)
                curr = ''
            else:
                curr += i
        return '/'+'/'.join(stk)
