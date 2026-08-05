class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li=list()
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    li=[i,j]                        
                    return li
# s=Solution()
# lis=[2,7,11,15]
# tar=9
# s.twoSum(lis,tar)


        