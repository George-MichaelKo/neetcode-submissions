class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {'+','-','*','/'}
        stack = []
        for t in tokens:
            if t not in op:
                stack.append(t)
            else:
                r = int(stack.pop())
                l = int(stack.pop())
                if t == '+':
                    eq = l + r
                elif t == '-':
                    eq = l - r
                elif t == '*':
                    eq = l * r
                else:
                    eq = l / r
                stack.append(eq)
        return int(stack[-1])
        