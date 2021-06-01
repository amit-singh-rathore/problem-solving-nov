class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        three = 0
        five = 0
        for i in range(1, n+1):
            three += 1
            five += 1
            
            if(three == 3 and five == 5):
                result.append("FizzBuzz")
                three = 0;
                five =0;
                continue
            elif(three == 3):
                result.append("Fizz")
                three = 0
                continue
            elif(five == 5):
                result.append("Buzz")
                five = 0
                continue
            else:
                result.append(str(i))

        return result
        