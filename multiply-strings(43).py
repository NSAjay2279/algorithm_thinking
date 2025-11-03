class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if int(num1) < 10 or int(num2) < 10:
            return str(int(num1) * int(num2))
        else:
            n = max(len(str(num1)), len(str(num2)))
            half = n // 2
            a = str(int(num1) // (10 ** (half)))
            b = str(int(num1) % (10 ** (half)))
            c = str(int(num2) // (10 ** (half)))
            d = str(int(num2) % (10 ** (half)))
            ac = int(self.multiply(a, c))
            bd = int(self.multiply(b, d))
            ad_plus_bc = int(self.multiply(str(int(a)+int(b)), str(int(c)+int(d))))-ac-bd
            return str(ac * (10 ** (2 * half)) + (ad_plus_bc * (10 ** half)) + bd)

            # T.C - O(n^1.58)
             
            
