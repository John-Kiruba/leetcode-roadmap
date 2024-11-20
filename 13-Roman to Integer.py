class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        prev = 0
        le = len(s)
        for i in range(le):
            value = roman_map[s[::-1][i]]
            if value < prev:
                total -= value
            else:
                total += value
            prev = value
        
        return total


s = Solution()
s.romanToInt('MCMXCIV')