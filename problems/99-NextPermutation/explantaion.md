# Explanation

Find the largest index k such that `a[k] < a[k + 1]`. If no such index exists, the permutation is the last permutation.
Find the largest index l greater than k such that `a[k] < a[l]`.
Swap the value of `a[k]` with that of `a[l]`.
Reverse the sequence from `a[k + 1]` up to and including the final element `a[n]`.


