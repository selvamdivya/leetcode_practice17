class Solution:
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= temp + temp:
                temp = temp + temp
                multiple = multiple + multiple

            dividend = dividend - temp
            quotient = quotient + multiple

        if negative:
            quotient = -quotient

        if quotient > INT_MAX:
            quotient = INT_MAX

        if quotient < INT_MIN:
            quotient = INT_MIN

        return quotient