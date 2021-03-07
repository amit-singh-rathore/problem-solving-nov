# Explanation

- If X > Y, Only way is to keep decreasing untill we reach to Y, ```X - Y```
- If X == Y, then we already happy and we return 0.
For moving from X to Y we can either double or substract. but doubling may overshoot and decrements to reach to Y may be too expensive.
If we work from Y and try to reach X we wont overshoot by a huge margin as every time the gap between target is reduing.
Since we are reversing the direction we will reverse the operations (double -> half) (substraction -> addition)


