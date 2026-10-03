class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0]*len(temperatures)
        stack = [0]

        # while current element is greater tahn previous elements pop and add to results 
        for i in range(1, len(temperatures)):
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
                continue

            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                results[index] = i - index
            
            stack.append(i)
            
        return results 
        