from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        for word in strs[1:]:
            print(prefix)
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

s= Solution()
s.longestCommonPrefix(['aaa','aa','aaa'])