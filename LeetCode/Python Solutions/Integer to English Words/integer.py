class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def helper(n):
            if n == 0:
                return []
            if n < 20:
                return [ones[n]]
            if n < 100:
                return [tens[n // 10]] + helper(n % 10)
            if n < 1000:
                return [ones[n // 100], "Hundred"] + helper(n % 100)
        
        words = []
        for i in range(len(thousands)):
            if num % 1000 != 0:
                words = helper(num % 1000) + [thousands[i]] + words
            num //= 1000
        
        return ' '.join([word for word in words if word])