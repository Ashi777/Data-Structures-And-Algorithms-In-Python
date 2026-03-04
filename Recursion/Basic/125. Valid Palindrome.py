'''class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        return cleaned == cleaned[::-1]
'''

class Solution(object):
    def isPalindrome(self, s):
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        return self.helper(cleaned)

    def helper(self, sub):
        # Base case: empty string or single char
        if len(sub) <= 1:
            return True
        # Compare first and last
        if sub[0] != sub[-1]:
            return False
        # Recurse on inner substring
        return self.helper(sub[1:-1])
