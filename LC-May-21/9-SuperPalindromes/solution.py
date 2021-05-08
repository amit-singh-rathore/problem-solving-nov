class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_palindrome(n):
            return int(str(n)[::-1]) == n

        res = 0;
        l = int(left)
        r = int(right)

        palindrome = []

        for i in range(1, 10):
            palindrome.append(i)

        for i in range(1, 10000):
            s1 = str(i)
            s2 = str(i);
            s2 = "".join(reversed(s2))
            p = int(s1+s2)
            if p > math.sqrt(r):
                break
            else:
                palindrome.append(int(s1+s2))

            for j in range(10):
                temp = s1
                temp += str(j)
                temp += s2;
                if int(temp) > math.sqrt(r):
                    break
                else:
                    palindrome.append(int(temp))

        for item in palindrome:
            num = item * item
            if(num <= r and num >=l and is_palindrome(num)):
                res += 1

        return res