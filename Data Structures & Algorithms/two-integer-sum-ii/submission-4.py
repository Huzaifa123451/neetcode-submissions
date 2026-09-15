class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        for i in range(start,len(numbers)):
            next = start + 1
            for j in range(next,len(numbers)):
                if numbers[start] + numbers[next] == target:
                    return [start+1,next+1] 
                next += 1
            start +=1
       