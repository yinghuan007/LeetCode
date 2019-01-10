class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        dup = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[dup]:
                dup += 1
                nums[dup] = nums[i]
        return dup + 1
