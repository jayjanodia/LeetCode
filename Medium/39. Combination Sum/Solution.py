# Reference: https://www.youtube.com/watch?v=GBKI9VSKdGg&t=268s

# Logic
# We must find the combination of each number
# Let's say we have [2, 3, 6, 7]. So then initially, we have just 2, 3, 6, 7. Now check if the value is equal to the target 
# or greater than the target. If the value is equal, then append that number to a list. Otherwise, break that loop. If the
# value is less than the target then repeat the process for all numbers. So now, we would have 2, 2; 2, 3; 2, 6; 2, 7;
# 3, 2; 3, 3; 3, 6; 3, 7       6;2 (break since 6 + 2 > 7), 7 has already been broken since it is equal to the target

def combinations(candidates, target):
    outcome = []

    def dfs(i, cur, total):
        if total == target:
            outcome.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return

        # Including the candidate
        total = total + candidates[i]
        cur.append(candidates[i])
        dfs(i, cur, total) 

        # Not including the candidate (not repeating)
        cur.pop()
        total = total - candidates[i]
        dfs(i+1, cur, total)
    
    dfs(0, [], 0)
    return outcome


print(combinations([2,3,6,7], 7))