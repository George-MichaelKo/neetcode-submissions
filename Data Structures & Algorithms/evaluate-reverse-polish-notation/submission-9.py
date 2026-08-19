class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {'+','-','*','/'}
        stack = []
        for t in tokens:
            if t not in op:
                stack.append(int(t))
            else:
                r = stack.pop()
                l = stack.pop()
                if t == '+':
                    eq = l + r
                elif t == '-':
                    eq = l - r
                elif t == '*':
                    eq = l * r
                else:
                    eq = int(l / r)
                stack.append(eq)
        return stack[-1]
        