# 745. Prefix and Suffix Search

Design a special dictionary which has some words and allows you to search the words in it by a prefix and a suffix.

Implement the WordFilter class:

- WordFilter(string[] words) Initializes the object with the words in the dictionary.
- f(string prefix, string suffix) Returns the index of the word in the dictionary which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.

## Example:
```

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

```