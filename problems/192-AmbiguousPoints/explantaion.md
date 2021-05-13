# Explanation

For each place to put the comma, we separate the string into two fragments. For example, with a string like "1234", we could separate it into fragments "1" and "234", "12" and "34", or "123" and "4".

Then, for each fragment, we have a choice of where to put the period, to create a list make(...) of choices. For example, "123" could be made into "1.23", "12.3", or "123".

        