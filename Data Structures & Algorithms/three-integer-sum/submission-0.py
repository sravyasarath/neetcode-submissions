class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i, n in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if n>0:
                break    
            l,r=i+1,len(nums)-1
            while l<r:
                s=n+nums[l]+nums[r]
                if s>0:
                    r=r-1
                elif s<0:
                    l=l+1
                else:
                    res.append([n,nums[l],nums[r]])
                    l=l+1
                    r=r-1
                    while nums[l]==nums[l-1] and l<r:
                        l=l+1
                    while nums[r]==nums[r+1] and l<r:
                        r=r-1  
        return res           