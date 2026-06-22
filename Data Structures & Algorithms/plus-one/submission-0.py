class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        i = 0
        digits.reverse()

        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = False
            else:
                digits.append(1)
                carry = False
            i += 1
        
        digits.reverse()
        return digits
