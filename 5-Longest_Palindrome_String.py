from operator import indexOf


class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '^#' + '#'.join(s) + '#$'
        n = len(t)
        p = [0] * n
        center = right_boundary = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i

            if i < right_boundary:
                p[i] = min(right_boundary - i, p[mirror]) # creates a additive value that wil be used for finding palindrome range

            # check for palindrome on either sides of center; But instead of having a
            # pointer as center, index created by i and line:15 serves as aggregator.
            while t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1

            if i + p[i] > right_boundary:
                center = i
                right_boundary = i + p[i] #notice here, i + p[i] works with line:18; it represents the next set of palindrome
                                          #right boundary limit

        max_len = max(p)
        center_index = p.index(max_len)
        start = (center_index - max_len) // 2
        return s[start: start + max_len]


s=Solution()
print(s.longestPalindrome('cbbd'))