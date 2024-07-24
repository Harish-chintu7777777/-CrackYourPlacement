class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b = a[::-1],b[::-1]
        res = ""
        carry = 0
        for i in range(max(len(a),len(b))):
            A = ord(a[i]) - ord("0") if i<len(a) else 0
            B = ord(b[i]) - ord("0") if i<len(b) else 0

            s = A+B+carry
            char = str(s%2)
            res += char
            carry = s//2
        if carry:
            res = "1" + res[::-1]
            return res
        return res[::-1]
