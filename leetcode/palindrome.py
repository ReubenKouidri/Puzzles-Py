"""
A phrase is a palindrome if, after converting all uppercase letters
 into lowercase letters and removing all non-alphanumeric characters,
 it reads the same forward and backward.
 Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

import re


def is_palindrome(s: str):
    ns = re.sub(r'[\W_]+', '', s.lower())
    ns_rev = ns[::-1]
    return ns == ns_rev


def is_palindrome_noregex(s: str):
    cleaned = "".join(char for char in s.lower() if char.isalnum())
    return cleaned == cleaned[::-1]


def test():
    assert is_palindrome("A man, a plan, a canal:_ Panama") is True
    assert is_palindrome_noregex("A man, a plan, a canal:_ Panama") is True
    print("PASSED")


if __name__ == "__main__":
    test()
