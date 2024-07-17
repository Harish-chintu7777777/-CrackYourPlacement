class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()
        chk=strs[0]
        strs.remove(strs[0])
        res=""
        for i in range(len(chk)):
            flag=0
            for j in strs:
                if chk[i] ==j[i]:
                    flag+=1
                else:
                    break
            if flag==len(strs):
                res+=chk[i]
            else:
                break
        if len(res)==0:
            return ""
        return (res)
