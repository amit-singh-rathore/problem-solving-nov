# Max Continuous Series of 1s

Given an array of **1s** and **0s**, an integer **m**, where **m** signifies max number of flips allowed, Find the positions of Zeros which when flipped will produce longest continuous series of 1s.

#### Example:
array = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]

m = 2

Output: [5, 7]

Explanation: We are allowed to flip the maximum of 2 zeroes. If we flip array[5] and array[7], we get 8 consecutive 1’s which is longest possible continuous series of 1s

## Example

```Input: A[] = {-7, 1, 5, 2, -4, 3, 0}
Output: 3
Explanation: 3 is an equilibrium index, because:
a[0] + a[1] + a[2] = a[4] + a[5] + a[6]```






