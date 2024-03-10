"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
of rows like this:

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a
number of rows:

string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""


def zigzag(s, rows):
    if rows == 1 or rows >= len(s):
        return s

    inc = 2 * rows - 2
    n = len(s)

    result = ""

    for i in range(min(n, rows)):
        result += s[i]
        # right_i is the actual index of
        # the char on the vertical line
        # right_i = inc + i | left_i = (inc + i) - 2*i
        left_i, right_i = inc - i, inc + i

        while left_i < n:
            # If it is not the first or last row
            if i != 0 and i != rows - 1:
                result += s[left_i]
            # If right_i is still a valid index
            if right_i < n:
                result += s[right_i]

            left_i += inc
            right_i += inc

    return result


def test():
    assert zigzag("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert zigzag("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"


if __name__ == "__main__":
    test()
