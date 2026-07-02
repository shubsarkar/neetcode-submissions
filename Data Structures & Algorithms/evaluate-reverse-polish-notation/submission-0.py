class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # need to take a stack for this
        stack = []

        for item in tokens:
            if item == "+":
                stack.append(stack.pop() + stack.pop())
            elif item == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif item == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            elif item == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(item)) # it's a num

        return stack[0]
            
        

