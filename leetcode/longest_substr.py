"""
Given a string s, find the length of the longest substring
 without repeating characters.

Def: A substring is a contiguous non-empty sequence of characters
     within a string.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a
substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


def longest_substring(s):
    d = dict()
    l, max_len = 0, 0
    for r, char in enumerate(s):
        if d.get(char) is None:
            d[char] = 1
        else:
            d[char] += 1
            while d[char] > 1 and l <= r:
                d[s[l]] -= 1
                l += 1

        max_len = max(max_len, r - l + 1)

    return max_len


def test():
    assert longest_substring("abcabcbb") == 3
    assert longest_substring("bbbbb") == 1
    assert longest_substring("pwwkew") == 3
    print("PASSED!")


if __name__ == "__main__":
    test()
