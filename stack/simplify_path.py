class Solution:
    def simplifyPath(self, path: str) -> str:
        items = path.split("/");
        acc = [];
        for item in items:
            if (item == "/" or item == "" or item == "."): continue;
            elif (item == ".."):
                if (len(acc) > 0): acc.pop();
                else: continue;
            else:
                acc.append(item);
        return "/" + '/'.join(acc);
    
if __name__ == "__main__":
    sol = Solution();
    print(sol.simplifyPath("/home/"))
    print(sol.simplifyPath("/home//foo/"))
    print(sol.simplifyPath("/home/user/Documents/../Pictures"))
    print(sol.simplifyPath("/../"))
    print(sol.simplifyPath("/.../a/../b/c/../d/./"))