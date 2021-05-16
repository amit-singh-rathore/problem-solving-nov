# Explanation

We place the stick at end. We have two cases in that scenario.
case 1: 
If the stick at the end is largest, our problem reduces to (n-1, k-1)
`dp[(n, k)] += dfs((n - 1, k - 1))

case 2: If the stick is not the largest, our problem comes down to (n-1, k).
For this the equation is
`dp[(n, k)] += dfs((n - 1, k)) * (n - 1)`
Extra (n-1) comes from the fact that all sticks not equal to largets stick will be (n-1)

Edge case 1
if n == k, return 1;
Edge case 2
if k == 0, return 0;