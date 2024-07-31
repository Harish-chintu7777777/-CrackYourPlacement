class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=len(nums2)
        l1=[]
        l,stk=[],[]

        for i in range(s-1,-1,-1):
            if len(stk)==0:
                stk.append(nums2[i])
                l.append(-1)
            elif len(stk)>0 and stk[-1]>nums2[i]:
                l.append(stk[-1])
                stk.append(nums2[i])
            elif len(stk)>0 and stk[-1]<=nums2[i]:
                while(len(stk)>0 and stk[-1]<=nums2[i]):
                    stk.pop()
                if len(stk)==0:
                    l.append(-1)
                    stk.append(nums2[i])
                else:
                    l.append(stk[-1])
                    stk.append(nums2[i])
                    
            else:
                stk.append(nums2[i])
        x=(l[::-1])
        for i in nums1:
            l1.append(x[nums2.index(i)])
        return l1
