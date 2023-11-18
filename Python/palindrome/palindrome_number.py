class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        reversed_x = x_str[::-1]
        return reversed_x == x_str