class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        dup = -1
        for i in range(0,len(nums)):
            if nums[i] != val:
                dup += 1
                nums[dup] = nums[i]
        return dup + 1
