class Solution:
    def multiply(self, num1, num2):
        
        # If either number is 0
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        # Maximum result length = m + n
        result = [0] * (m + n)

        # Multiply digits from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                product = digit1 * digit2

                # Positions where the result is stored
                pos1 = i + j
                pos2 = i + j + 1

                total = product + result[pos2]

                result[pos2] = total % 10
                result[pos1] += total // 10

        # Convert array to string and remove leading zeros
        answer = ''.join(map(str, result)).lstrip('0')

        return answer