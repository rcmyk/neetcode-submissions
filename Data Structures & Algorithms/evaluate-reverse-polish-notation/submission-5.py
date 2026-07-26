import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:
            if tok in "+-*/":
                b, a = stack.pop(), stack.pop()
                match tok:
                    case "+": stack.append(a + b)
                    case "-": stack.append(a - b)
                    case "*": stack.append(a * b)
                    case "/": stack.append(math.trunc(a / b))
            else:
                stack.append(int(tok))

        return stack.pop()