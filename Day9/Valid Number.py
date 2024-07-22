class Solution:
    def isNumber(self, s: str) -> bool:
        seenDot, seenExponent, seenDigit = False, False, False

        for i,c in enumerate(s):
            if c.isdigit():
                seenDigit = True
            elif c in ('+', '-'):
                if not (i == 0 or s[i-1] in ('e', 'E')):
                    return False
            elif c in ('e', 'E'):
                if seenExponent or not seenDigit:
                    return False
                seenExponent = True
                seenDigit = False
            elif c == '.':
                if seenExponent or seenDot:
                    return False
                seenDot = True
            else:
                return False
        return seenDigit            
        
