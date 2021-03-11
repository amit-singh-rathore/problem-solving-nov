def intToRoman(num):
    symbol = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    i = len(values)-1
    res = ""
    number = num
    while number:
        div = number//values[i]
        number %= values[i]
        while div:
            res += symbol[i] 
            div -= 1
        i -= 1
    return res
          