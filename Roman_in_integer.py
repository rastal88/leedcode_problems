class Solution:
    def roman_to_int(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        rcheck = 0
        for i in range(len(s)):
            current = roman[s[i]]
            if current > rcheck:
                ans += current - 2 * rcheck
            else:
                ans += current
            rcheck = current
        return ans
