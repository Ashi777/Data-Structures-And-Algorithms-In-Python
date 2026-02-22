class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Dictionary to store mapping of characters from s to t
        mapping_s_t = {}
        # Set to keep track of already mapped characters in t
        mapped_t = set()

        for char_s, char_t in zip(s, t):
            if char_s in mapping_s_t:
                if mapping_s_t[char_s] != char_t:
                    return False
            else:
                if char_t in mapped_t:
                    return False
                mapping_s_t[char_s] = char_t
                mapped_t.add(char_t)

        return True
