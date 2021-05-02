# Explanation

We have implemented this using dictionary. We generate prefix+#+suffix for each word. This will create n^2 keys for a word. 
When we do a lookup we create the key in the same way and get its value in the mapping.

Alternative solution is to use Trie. ( 1 for prefix and another for suffix)

We can even improve upon the above mentioned Trie solution by having Suffix Wrapped Words. 
