class Solution:
    def insert(self, intervals, newInterval):
        result = []

        for interval in intervals:

            # Current interval is before newInterval
            if interval[1] < newInterval[0]:
                result.append(interval)

            # Current interval is after newInterval
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval

            # Overlapping intervals
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        # Add the final newInterval
        result.append(newInterval)

        return result