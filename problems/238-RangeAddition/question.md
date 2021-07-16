# 370. Range Addition

You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].

You have an array arr of length length with all zeros, and you have some operation to apply on arr. In the ith operation, you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.

Return arr after applying all the updates.

## Example

```
Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]

```

## Constraints

```
- 1 <= length <= 10^5
- 0 <= updates.length <= 10^4
- 0 <= startIdxi <= endIdxi < length
- -1000 <= inc <= 1000

```