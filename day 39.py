class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, target, combination):
            if target == 0:
                result.append(combination[:])
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                combination.append(candidates[i])

                # i is used again because the same number
                # can be chosen unlimited times
                backtrack(i, target - candidates[i], combination)

                combination.pop()

        backtrack(0, target, [])
        return result