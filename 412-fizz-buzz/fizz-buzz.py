class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        li=[]
        for i in range(1,n+1):
            if i%3!=0 and i%5 !=0:
                li.append(str(i))
            if i%3==0 and i%5==0:
                li.append("FizzBuzz")
                continue
            if i%3==0:
                li.append("Fizz")
            if i%5==0:
                li.append("Buzz")
        return li
