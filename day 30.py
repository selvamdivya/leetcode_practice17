class Solution:
    def findSubstring(self, s, words):
        from collections import Counter

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        target = Counter(words)
        result = []

        for start in range(word_len):
            left = start
            count = 0
            current = Counter()

            for right in range(start, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word not in target:
                    current.clear()
                    count = 0
                    left = right + word_len
                    continue

                current[word] += 1
                count += 1

                while current[word] > target[word]:
                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len
                    count -= 1

                if count == word_count:
                    result.append(left)

                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len
                    count -= 1

        return result