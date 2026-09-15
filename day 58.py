class Solution:
    def lengthOfLastWord(self, s):
        # Remove spaces at the beginning and end
        s = s.strip()

        # Split the string into words
        words = s.split()

        # Return the length of the last word
        return len(words[-1])