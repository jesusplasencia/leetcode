class Solution:
    def intToRoman(self, num: int) -> str:
        """
        >>> intToRoman(1994)
        MCMXCIV
        """
        word = []
        book = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }

        for key, val in reversed(book.items()):
            while num > 0:
                if num >= val:
                    word.append(key)
                    num = num - val
                else:
                    break

        return "".join(word)


if __name__ == "__main__":
    sol = Solution()
    print(sol.intToRoman(3390))
