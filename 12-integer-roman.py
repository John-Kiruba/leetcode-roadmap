class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1: 'I', 4: 'IV', 5:'V', 9: 'IX', 10: 'X', 40:'XL', 50:'L', 90:'XC', 100: 'C', 400 : 'CD', 500: 'D', 900: 'CM', 1000: 'M' }

        def romanize(num, arr):

            if num <= 0 :
                return  ""
            ret = ''
            for i in arr[::-1]:
                if num >= i:
                    ret += roman[i] + romanize(num - i, arr)
                    return ret
        return romanize(num,list( roman.keys()))



#best:
class Solution:
    def intToRoman(self, num: int) -> str:
        # Define Roman numeral symbols and values
        roman_symbols = [
            ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
            ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
        ]

        result = ""

        # Iterate through the Roman numeral values and symbols
        for symbol, value in roman_symbols:
            while num >= value:
                result += symbol  # Append the Roman numeral symbol
                num -= value  # Subtract the corresponding value

        return result