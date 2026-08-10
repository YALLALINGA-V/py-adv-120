class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        li=[]
        l=0
        n=len(s)
        count={}
        for r in range(9,n):
            curr=s[l:r+1]
            if curr not in count:
                    count[curr]=1
            else:
                    if count[curr]==1:
                        li.append(curr[:])
                        count[curr]+=1
            l+=1
        return li

                   
        return li
        