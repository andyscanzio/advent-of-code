def p(n, memo={}):
    # Base cases
    if n == 0:
        return 1
    if n == 1:
        return 1
    # Check if the value of p(n) is already stored in the dictionary
    if n in memo:
        return memo[n]
    # Compute the value of p(n) using the recurrence relation
    p_n = p(n - 1) + p(n - 2) + p(n - 5) + p(n - 10)
    # Store the value of p(n) in the dictionary
    memo[n] = p_n
    return p_n


n = 0
while p(n) % 1000000 != 0:
    print(n)
    n += 1
print(n)
