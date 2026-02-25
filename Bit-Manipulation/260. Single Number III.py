class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for num in nums:
            xor_all ^= num
        diff_bit = xor_all & -xor_all    # Step 2: Find rightmost set bit
        a, b = 0, 0            # Step 3: Partition numbers
        for num in nums:
            if num & diff_bit:
                a ^= num
            else:
                b ^= num
        return [a, b]

