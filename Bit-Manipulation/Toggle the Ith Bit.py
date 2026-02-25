class Solution:
    def toggleIthBit(self, n: int, i: int) -> int:
        """
        Toggle (flip) the i-th bit of n.

        Args:
            n (int): The number.
            i (int): The bit position (0-indexed from LSB).

        Returns:
            int: Number after toggling the i-th bit.
        """
        return n ^ (1 << i)
