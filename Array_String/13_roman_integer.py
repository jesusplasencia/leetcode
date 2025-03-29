class Solution:
    def romanToInt(self, s: str) -> int:
        book = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        N = len(s)
        summ = 0

        for idx, char in enumerate(s):
            if idx < N - 1 and book[s[idx]] < book[s[idx + 1]]:
                summ = summ - book[char]
            else:
                summ = summ + book[char]

        return summ


if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("MCMXCIV"))
