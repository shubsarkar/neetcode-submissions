class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # tuple (temp, idx)
        result = [0] * len(temperatures) # result with the same length as temperatures 

        for idx, temp in enumerate(temperatures):
            
            while stack and temp > stack[-1][0]: # while the stack is not empty
                # for the first item there is nothing to compare with
                result[stack[-1][1]] = idx - stack[-1][1] # record the number of days
                stack.pop()
            
            stack.append((temp, idx))  # we push the element into the stack for later comparison    

        return result