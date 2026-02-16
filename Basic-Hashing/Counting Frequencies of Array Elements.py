class Solution:
    def countFrequencies(self, nums):
        # Your code goes here
        freq={}
        result=[]

        for num in nums:
            freq[num]=freq.get(num, 0)+1

        for num in freq:
            result.append([num, freq[num]])
        return result

