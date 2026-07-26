class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok in '+-*/':
                b = stack.pop()
                a = stack.pop()
                res = None
                if tok == '+': res = a + b
                elif tok == '-': res = a - b
                elif tok == '*': res = a * b
                elif tok == '/': res = math.trunc(a / b)
                else: raise Exception("Invalid Operator")
                stack.append(res)
            else:
                stack.append(int(tok))
        return stack[0]