def isValid(s):
    b_stack = []
    brace_map = {'(':')','[':']','{':'}'}
    for b in s :
        if b in brace_map:
            b_stack.append(brace_map[b])
        else:
            if not b_stack or b_stack.pop() != b:
                return False
    return not b_stack
    
print(isValid(")"))