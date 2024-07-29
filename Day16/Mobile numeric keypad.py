class Solution:
    def getCount(self, n):
        # Define adjacency list for the phone keypad
        m = {0: [0, 8],
             1: [1, 2, 4], 
             2: [1, 2, 3, 5], 
             3: [2, 3, 6], 
             4: [1, 4, 5, 7], 
             5: [2, 4, 5, 6, 8], 
             6: [3, 5, 6, 9], 
             7: [4, 7, 8], 
             8: [0, 5, 7, 8, 9], 
             9: [6, 8, 9]}
        
   
        memo = {}
        
        def count_sequences(length, digit):
        
            if length == 1:
                return 1
            
            if (length, digit) in memo:
                return memo[(length, digit)]
            
         
            total = 0
            for next_digit in m[digit]:
                total += count_sequences(length - 1, next_digit)
         
            memo[(length, digit)] = total
            return total
        
        return sum(count_sequences(n, digit) for digit in range(10))




