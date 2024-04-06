class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache = {v: i for i, v in enumerate(nums)}
        for i in range(len(nums)):
            j = cache.get(target - nums[i])
            if i != j and j is not None:
                return [i, j]