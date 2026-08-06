class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median=0
        mergedarray=nums1+nums2
        mergedarray.sort()
        n=len(mergedarray)
        if n%2==1:
            median=mergedarray[n//2]
        else:
             median=(mergedarray[(n//2)-1]+mergedarray[n//2])/2
        return median