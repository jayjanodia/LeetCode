# REFERENCE: https://www.youtube.com/watch?v=HAA8mgxlov8&t=1386s

def top_down(s, p):

    def dfs(i, j):
        # i will tell us what position we are at for s
        # j will tell us what position we are at for p
        # Base Case: If i is out of bounds and j is out of bounds that means we have found our solution.
        if i >= len(s) and j >= len(p):
            return True
        # If i is not out of bounds but j is out of bounds then that means that the string is not matched
        if j >= len(p):
            return False

        # Check that i is not out of bounds and that there is a match of the first character or if the first character is any character '.'
        match = i < len(s) and (s[i] == p[j] or p[j] == '.')

        # Check if the next character is a star. We know that the first character will never be a star
        # Also make sure that j+1 is in bounds
        if p[j+1] == '*' and j+1 < len(p):
            # Recursive calls for whether to use '*' or not
            return dfs(i, j+2) or (match or dfs(i+1, j)) # don't use star or use star.
        if match:
            return dfs(i+1, j+1)
        return False

    return dfs(0, 0)

