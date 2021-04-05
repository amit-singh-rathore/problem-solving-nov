# Explanation

We start with `[""]`. Then we generate new combo by adding the elments in the items of the list.

First we add a, b, c.
Then on abc we add (d, e, f) on each item one by one.

```
['a', 'b', 'c']
['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

```

We do this till we have reached the required length.


