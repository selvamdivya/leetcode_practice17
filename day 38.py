class Solution:
    def countAndSay(self, n):
        result = "1"

        for i in range(2, n + 1):
            next_string = ""
            count = 1

            for j in range(1, len(result)):
                if result[j] == result[j - 1]:
                    count += 1
                else:
                    next_string += str(count) + result[j - 1]
                    count = 1

            next_string += str(count) + result[-1]
            result = next_string

        return result