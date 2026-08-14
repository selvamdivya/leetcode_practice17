class Solution:
    def removeElement(self, nums, val):
        K = 0

        for num in nums:
            if num != val:
                nums[K] = num
                K += 1

        return K