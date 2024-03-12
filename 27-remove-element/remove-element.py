class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        new = []
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 0
                
            else:
                new.append(nums[i])
                count+=1
        for c in range(len(nums)):
            if c < len(new):
                nums[c] = new[c]
            else:
                nums[c] = 0
        return count
        

        
        