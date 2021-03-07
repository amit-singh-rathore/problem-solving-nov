# Explanation

## Sliding window solution — O(n)

We use sliding window as we need to find a continuous sum. For each item we need to only add the last item and remove i-w item from the sum. 
This way we only calculate perform one addition and one substraction for each item rather than doing *w* x *n* additions.