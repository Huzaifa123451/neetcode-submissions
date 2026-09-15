class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sum_so_far = 0
        result = 0
        stack = []
        for i in range (0,len(tokens)):
            if tokens[i] != "+" and tokens[i]  != "-" and tokens[i] != "*" and tokens[i] != "/":
                stack.append(int(tokens[i]))
            else:
                op = tokens[i]
                if len(stack) < 2:
                    return sum_so_far
                else:
                    num1 = stack.pop()
                    num2 = stack.pop()
                if op == "+": 
                    result = int(num1 + num2)
                elif op == "-":
                     result = int(num2 - num1)
                elif op == "*":
                     result = int(num1 * num2)
                else: 
                    result = int(num2 / num1)
                stack.append(result)
        val_to_return = stack.pop()
        
            

        return val_to_return
            