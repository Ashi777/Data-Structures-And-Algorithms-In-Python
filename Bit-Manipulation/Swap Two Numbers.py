class Solution:
    def swap(self, a, b):
        """
        Swap two integers and return them.

        Args:
            a (int): First integer.
            b (int): Second integer.

        Returns:
            Tuple[int, int]: The two integers, swapped.
        """
        # Your code goes here
        a=a^b
        b=a^b
        a=a^b
        return a, b

