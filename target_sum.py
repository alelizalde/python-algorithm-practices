class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        rtype = []
        tmpl = []
        sum = 0
        for num in nums:
            sum = sum + num
            if