class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        i = 0

        # Place each positive number x at index x - 1
        while i < n:
            correct_index = nums[i] - 1

            if 1 <= nums[i] <= n and nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        # Find the first index where the number is incorrect
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all numbers 1 to n are present
        return n + 1