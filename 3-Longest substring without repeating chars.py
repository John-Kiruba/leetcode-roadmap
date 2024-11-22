class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charset = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1

            charset.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
s = Solution()
ret = s.lengthOfLongestSubstring("abcabcbb")
print(ret)

#
# best answer :
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         l = answer = 0
#         chars = [-1]*128
#         for r, ch in enumerate(s):
#             if chars[ord(ch)] >= l:
#                 l = chars[ord(ch)] +1
#             else:
#                 answer = max(answer, r-l+1)
#             chars[ord(ch)] = r
#         return answer