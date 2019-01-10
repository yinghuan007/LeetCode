class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        head = 0
        tail = len(nums)
        while head < tail:
            mid = head + (tail - head) / 2
            if nums[mid] > target:
                tail = mid
            elif nums[mid] < target:
                head = mid + 1
            else:
                return mid
        return head
#another way
'''
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        if target in nums:
            for i in range(0,len(nums)):
                if nums[i] == target:
                    return i
        for i in range(1,len(nums)):
            
            if nums[i-1] < target < nums[i]:
                return i
        return len(nums)
'''
