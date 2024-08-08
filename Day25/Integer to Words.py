Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def numberToWords(self, num: int) -> str:
        
        if num == 0:
            return 'Zero'

        ones_map = {
            1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
...             11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
...             15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
...             19: 'Nineteen'
...         }
... 
...         tens_map = {
...             20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
...             60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'
...         }
... 
...         def get_string(n):
...             hundreds = n // 100
...             n = n % 100
...             res = ""
...             if hundreds:
...                 res += ones_map[hundreds] + " Hundred "
...             if n >= 20:
...                 tens, ones = n // 10, n % 10
...                 res += tens_map[tens * 10] + " "
...                 if ones:
...                     res += ones_map[ones] + " "
...             elif n:
...                 res += ones_map[n] + " "
...             return res.strip()
... 
...         post_fix = ["", "Thousand", "Million", "Billion"]
...         i = 0
...         res = []
... 
...         while num > 0:
...             v1 = num % 1000
...             if v1 > 0:
...                 s = get_string(v1)
...                 res.append(s + " " + post_fix[i])
...             i += 1
...             num = num // 1000
... 
...         res.reverse()
...         return " ".join(res).strip()
