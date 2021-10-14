# Reference: https://www.youtube.com/watch?v=3jvWodd7ht0

def isPalindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l+1, r-1
    return True

def palindrome_partition(palindrome):
    '''
    BRUTE FORCE APPROACH
    1. Start with the whole string. We know that the individual characters are palindromes.
    2. Start iterating for the string. So, for a string aab, we have 3 iterations: a, aa, aab.
    3. Check if the first and last character match. If they don't match get rid of that iteration. In this case, we get rid of aab.
    4. Now check for the next iterations. So, string aab, iteration 1: a. So then next iteration would be a or ab.
    5. Repeat steps 3 and 4 until the iterations don't reach the end point
    https://ibb.co/N9R3Vgh
    '''
    list_of_palindromes = []
    current_palindrome = []

    def dfs(i):
        if i >= len(palindrome):
            list_of_palindromes.append(current_palindrome.copy())
            return

        for j in range(i, len(palindrome)):
            if isPalindrome(palindrome, i, j):
                current_palindrome.append(palindrome[i:j+1])
                dfs(j+1)
                current_palindrome.pop()

    dfs(0)
    return list_of_palindromes

print(palindrome_partition('a'))