class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            #  each number associated with its count (number of time it shows up - in a dictionary)
        sorted_nums = sorted(counts, key=lambda x: counts[x], reverse=True) #sorts them in order of their count - ascending
        return sorted_nums[:k] #returns up until the k'th integer
        