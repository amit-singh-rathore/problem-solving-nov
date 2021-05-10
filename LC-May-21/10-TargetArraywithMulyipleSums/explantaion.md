# Explanation

We solve this by retracing the steps to create

```
[1, 1, 1] --> [1, 3, 1] --> [1, 3, 5] --> [9, 3, 5]

retrace:

[9, 3, 5] --> [1, 3, 5] --> [1, 3, 1] --> [1, 1, 1]

```

While retracing what we did was replaced max elemnet with 1. We keep doing this till we have all ones. 
