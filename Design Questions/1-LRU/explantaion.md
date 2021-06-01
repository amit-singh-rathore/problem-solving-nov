## Explanation

We use OrderedDictionary to implement the LRU cache. 
Whenever we perform the get action, we move that key to end.
Similarly when we do a put operation we check if key exist then we delete that and add that in the end.
