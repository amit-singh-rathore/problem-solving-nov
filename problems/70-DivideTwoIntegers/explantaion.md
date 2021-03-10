# Explanation

Division can be thought of a series of subtraction. We will use this to solve.

E.g. 10//3 = 3 If we keep on subtracting 3 from 10 until we get the remainder less the 3, and count no of subtraction will give quotient. 

```
10-3 = 7
7 - 3 = 4
4 -3 = 1
```

To make the algo faster we wont be subtracting divisor in linear fashion.
if we look closely we can see the actual subtraction happening from original like ```10-3, 10-6, 10-9```. This can be also represented as ```10-(3*1), 10-(3*2)...```.
What if we start with by subtracting 6 itself and then subtract 3 and add the multipler(1+2) we get the answer 3.

```
[1,2,4,8,16]
[3,6,12,24,48]
```
In the above pair of list if we subtract 48 from the number we get quotient 16, again we subtract 24 from the number we have quotient as (16+8). 
In these two operation we reduced the number by 72 (48+24) at the same time quotient become 24(16+8). Which is nothing but 72//3 = 24.