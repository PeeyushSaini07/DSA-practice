class Solution:

  def isPalindrome(self, x):
    # Negative numbers are not palindromes
    if x < 0:
      return False

    s = str(x)
    return s == s[::-1]