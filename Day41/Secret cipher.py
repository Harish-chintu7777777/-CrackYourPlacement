Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def binpow(self, a, b):
        MOD = 1000000007
        ans = 1
        while b > 0:
            if b % 2 != 0:  
                ans = (ans * a) % MOD
            a = (a * a) % MOD
            b //= 2  
        return ans
... 
...     def compress(self, s):
...         p = 31
...         n = len(s)
...         MOD = 1000000007
... 
...         hash = [0] * (n + 1)
...         ppow = [1] * (n + 1)
...         inv = [1] * (n + 1)
... 
...         for i in range(1, n + 1):
...             ppow[i] = (ppow[i - 1] * p) % MOD
...             inv[i] = self.binpow(ppow[i], MOD - 2)
... 
...         for i in range(n):
...             hash[i + 1] = (ord(s[i]) - ord('a') + 1) * ppow[i]
...             hash[i + 1] %= MOD
...             hash[i + 1] = (hash[i] + hash[i + 1]) % MOD
... 
...         ans = []
...         i = n
... 
...         while i >= 1:
...             if i % 2 != 0:  
...                 ans.append(s[i - 1])
...                 i -= 1
...                 continue
... 
...             m = i // 2
...             val1 = hash[m]
...             val2 = (hash[i] - hash[m] + MOD) % MOD
...             val2 = (val2 * inv[m]) % MOD
...             if val1 == val2:
...                 ans.append('*')
...                 i = m
...             else:
...                 ans.append(s[i - 1])
...                 i -= 1
... 
