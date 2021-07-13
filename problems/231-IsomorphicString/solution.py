class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}
        for item in zip(s, t):
            key, value = item
            if key in char_map:
                if char_map[key] != value:
                    return False
            elif value in char_map.values():
                return False
            else:
                char_map[key] = value

        return True