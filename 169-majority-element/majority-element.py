class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
            if d[i]>len(nums)/2:
                return i
        return 0
        