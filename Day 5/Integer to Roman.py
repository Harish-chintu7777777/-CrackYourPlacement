Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def intToRoman(self, num: int) -> str:
... 
...         m = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M",
...         4:"IV",9:"IX",40:"XL",90:"XC",400:"CD",900:"CM"}
...         v = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
...         res = ""
...         for i in v:
...             while(num >= i):
...                 res += m[i]
...                 num -= i
