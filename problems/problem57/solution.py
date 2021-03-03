def combination_generator(cur_valid_comb, valid_comb_set):
    for idx in range(len(cur_valid_comb)):
        new_comb = cur_valid_comb[:idx] +"()"+ cur_valid_comb[idx:]
        valid_comb_set.add(new_comb)
    return valid_comb_set

def generateParenthesis(n):
    valid_combinations = {"()"}
    if n == 1:
        return list(valid_combinations)
    
    for _ in range(1, n):
        new_valid_comb = set()
        for combination in valid_combinations:
            valid_comb_set = combination_generator(combination, new_valid_comb)
        valid_combinations = valid_comb_set
        
    return list(valid_combinations)

print(generateParenthesis(3))