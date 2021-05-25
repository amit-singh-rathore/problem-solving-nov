class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in '/+-*':
                op1 = stack.pop()
                op2 = stack.pop()
                if token == '/':
                    val = op2 / op1
                elif token == '+':
                    val = op2 + op1
                elif token == '-':
                    val = op2 - op1
                elif token == '*':
                    val = op2 * op1
                stack.append(int(val))
            else:
                stack.append(int(token))
        return stack[0]