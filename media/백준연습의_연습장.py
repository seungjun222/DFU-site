def combination(n,r):
    if dp[n][r] != 0:
        return dp[n][r]
    if r == 1:
        return n
    elif n == r:
        return 1
    else:
        dp[n][r] = combination(n-1, r) + combination(n-1, r-1)

    return dp[n][r]

if __name__ == "__main__":
    r,n = map(int, input().split(" "))
    dp = [ [0 for _ in range(r+1)] for _ in range(n+1)]
    ans = combination(n,r)
    print(ans)
