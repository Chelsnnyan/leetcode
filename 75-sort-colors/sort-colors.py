class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c0=0
        c1=0
        c2=0
        for i in range(len(nums)):
            if nums[i] ==0:
                c0 +=1
            elif nums[i]==1:
                c1+=1
            else:
                c2+=1

        for i in range(len(nums)):
            if c0>0:
                nums[i] = 0
                c0-=1
            elif c0==0 and c1>0:
                nums[i] =1
                c1-=1
            else:
                nums[i] =2