class Solution:
    def reverse(self, x: int) -> int:
        s=[]
        y=x
        if  x<0:
            x=int(str(x)[1:])
        while x>0:
            temp=x%10
            s.append(temp)
            x//=10
        s.reverse()
        # for i in s:
        #     x=int("".join(map(str,s)))
        # return x
        result = sum(d * 10**i for i, d in enumerate(s))
        if  result  >2**31 -1 or result<-2**31:
            return 0
        if y<=0:
            result*=-1
        return result
