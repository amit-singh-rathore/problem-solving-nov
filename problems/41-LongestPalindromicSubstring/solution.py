def longestPalindrome(s):
    if len(s)==0: 
        return 0
    elif len(s)==1:
        return s
    max_len=1 
    start=0
    for i in range(1,len(s)):
    	if i-max_len >= 1:
            if s[i-max_len-1:i+1] == s[i-max_len-1:i+1][::-1]:
                start = i-max_len-1 
                max_len += 2
                continue
    	if i-max_len >= 0: 
            if s[i-max_len:i+1] == s[i-max_len:i+1][::-1]:
                start = i-max_len
                max_len += 1
    return s[start:start+max_len]

print(longestPalindrome('ababcgdjhg'))