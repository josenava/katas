"""There is a strange printer with the following two special properties:

    The printer can only print a sequence of the same character each time.
    At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.

Given a string s, return the minimum number of turns the printer needed to print it.


Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".

Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.

"""

def strange_printer(s: str) -> int:
    memo = {}
    def dp(i, j):
        if i > j: return 0
        if (i, j) not in memo:
            ans = dp(i+1, j) + 1
            for k in range(i+1, j+1):
                if s[k] == s[i]:
                    ans = min(ans, dp(i, k-1) + dp(k+1, j))
            breakpoint()
            memo[i, j] = ans
        return memo[i, j]

    breakpoint()
    return dp(0, len(s) - 1)


if __name__ == "__main__":
    assert 5 == strange_printer("abcabc")

