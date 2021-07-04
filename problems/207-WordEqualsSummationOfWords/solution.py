class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        char_order = { char: str(idx) for idx, char in enumerate('abcdefghijklmnopqrstuvwxyz')}
        
        def get_integer_value(word):
            int_rep = "".join([char_order[char] for char in word])
            return int(int_rep)
        
        return (get_integer_value(firstWord) + get_integer_value(secondWord)) == get_integer_value(targetWord)