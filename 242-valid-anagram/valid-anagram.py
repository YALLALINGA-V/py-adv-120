class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        d1={}
        for i in s:
            if i in d:
                 d[i]+=1
            else:
                d[i]=1
        c=0
        for j in t:
            if j in d1:
                d1[j]+=1
            else:
                d1[j]=1 
        if d1.items()==d.items():
            return True
        else:
            return False

        