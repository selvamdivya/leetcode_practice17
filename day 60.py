class Solution:
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n + 1)]
        ans = ""

        factorial = 1

        for i in range(1, n):
            factorial *= i

        k = k - 1

        for i in range(n, 0, -1):
            index = k // factorial
            k = k % factorial

            ans += nums[index]
            nums.pop(index)

            if i > 1:
                factorial = factorial // (i - 1)

        return ans