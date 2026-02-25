class Solution:
    def removeLastSetBit(self, n: int) -> int:
        """
        Remove the rightmost set bit from n.

        Args:
            n (int): The number.

        Returns:
            int: Number after removing the rightmost set bit.
        """
        return n & (n - 1)

