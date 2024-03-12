class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        for x in nums:
            if nums.count(x) > l//2:
                return x
        