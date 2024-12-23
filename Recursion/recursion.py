class Solution:
    def factor(self, n: int) -> int:
        if (n == 0): return 0;
        elif (n == 1): return 1;
        return self.factor(n - 1) + self.factor(n - 2);
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.factor(4));