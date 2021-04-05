class Solution:
    def create_combo(self, curr_str, letters):
        new_q = [curr_str + letter for letter in letters]
        return new_q
    
    def letterCombinations(self, digits: str) -> List[str]:
        mapping  = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z'],
        }
        
        if not digits:
            return []
        
        q = [""]
        for i in range(len(digits)):
            letters = mapping[digits[i]]
            new_list = []
            for base in q:
                new_list.extend(self.create_combo(base, letters))
            q = new_list
        return q
        
        