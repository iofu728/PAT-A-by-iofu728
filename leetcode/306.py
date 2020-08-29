# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-28 16:14:47
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-28 16:15:26

"""
306. Additive Number Medium
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199

Constraints:

num consists only of digits '0'-'9'.
1 <= num.length <= 35
Follow up:
How would you handle overflow for very large input integers?

Accepted 52,501 Submissions 178,845
"""


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def is_ok(a: int, b: int):
            print(a, b)
            a, b = num[:ii], num[ii : ii + jj]
            if (
                (len(a) > 1 and a[0] == "0")
                or (len(b) > 1 and b[0] == "0")
                or (len(a) == 0)
                or (len(b) == 0)
            ):
                return False
            a, b = int(a), int(b)
            end = ii + jj
            if end == N:
                return False
            while end < N:
                print("=", a, b, end)
                a, b = b, (a + b)
                if int(num[end : end + len(str(b))]) != b or (
                    len(str(b)) > 1 and num[end : end + len(str(b))][0] == "0"
                ):
                    return False
                end += len(str(b))
            return True

        N = len(num)
        if N < 3:
            return False
        for ii in range(1, N // 3 + 2):
            for jj in range(1, (N - ii) // 2 + 2):
                if is_ok(ii, jj):
                    return True
        return False
