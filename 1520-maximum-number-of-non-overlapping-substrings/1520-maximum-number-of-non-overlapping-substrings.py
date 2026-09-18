class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = [len(s)] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        # Try to create a valid substring starting
        # from first occurrence of each character
        for i in range(len(s)):

            x = ord(s[i]) - ord('a')

            # Only start from first occurrence
            if first[x] != i:
                continue

            end = last[x]
            j = i
            valid = True

            while j <= end:
                y = ord(s[j]) - ord('a')

                # This character appeared before i
                if first[y] < i:
                    valid = False
                    break

                # Need to include all occurrences of this character
                end = max(end, last[y])

                j += 1

            if valid:
                intervals.append((i, end))

        # Choose non-overlapping intervals
        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for start, end in intervals:
            if start > prev_end:
                ans.append(s[start:end + 1])
                prev_end = end

        return ans