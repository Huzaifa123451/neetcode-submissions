class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        distance = 0
        list_to_return = [0 for i in range(len(temperatures))]
        stack = []
        for i in range(0,len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()                
                list_to_return[prev_index] = i - prev_index
            stack.append(i)
        return list_to_return