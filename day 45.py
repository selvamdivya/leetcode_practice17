class Solution:
    def jump(self, nums):
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):

            # Find the farthest position we can reach
            farthest = max(farthest, i + nums[i])

            # Reached the end of the current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps