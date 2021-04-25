class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for c in path:
            if c == "/" or c == "." or c == "":
                continue
            elif c != "..":
                stack.append(c)
            else:
                if stack:
                    stack.pop()
        return "/" + "/".join(stack)