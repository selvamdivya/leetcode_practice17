class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):
            # Find how many words can fit in this line
            j = i
            line_length = 0

            while j < len(words):
                if line_length + len(words[j]) + (j - i) > maxWidth:
                    break

                line_length += len(words[j])
                j += 1

            # Words in current line
            line_words = words[i:j]
            gaps = len(line_words) - 1

            # Last line or only one word
            if j == len(words) or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                result.append(line)

            else:
                # Total spaces needed
                total_spaces = maxWidth - sum(len(word) for word in line_words)

                # Spaces for each gap
                spaces = total_spaces // gaps
                extra = total_spaces % gaps

                line = ""

                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (spaces + (1 if k < extra else 0))

                line += line_words[-1]

                result.append(line)

            i = j

        return result