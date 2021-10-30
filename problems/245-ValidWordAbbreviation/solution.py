
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        idx, num = 0, 0
        for char in abbr:
            if char.isdigit():
                if num == 0 and char == '0':
                    return False
                num = int(char) + 10*num
            else:
                idx, num = idx + num, 0
                if idx >= len(word) or word[idx] != char:
                    return False
                idx += 1
        if (idx + num) == len(word):
            return True
        return False