class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #dictionary storing values to indexes
        d={}
        for x, y in enumerate(nums):
            #variable for the difference
            diff = target-y
            if diff in d:
                return [d[diff], x]
            else:
                d[y] = x
        return -1





