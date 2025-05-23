class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        ans = ""
        group = 0
        while num > 0:
            if num % 1000 != 0:
                local_results = ""
                part = num % 1000

                if  part >= 100:
                    local_results += ones[part // 100] + " Hundred "
                    part %= 100

                if part >= 20:
                    local_results += tens[part // 10] + " "
                    part %= 10
                
                if part > 0:
                    local_results += ones[part] + " "
            
                local_results += thousands[group] + " "
                ans = local_results + ans
            num //= 1000
            group += 1
        return ans.strip()