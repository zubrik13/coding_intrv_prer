class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        nums = []
        for char in s:
            if char in '0123456789':
                nums.append(char)
            else:
                letters. append(char)
        
        if abs(len(letters) - len(nums)) > 1:
            return ""
        
        if len(letters) < len(nums):
            short = letters
            long = nums
            extra = nums[-1]
        elif len(letters) == len(nums):
            short = letters
            long = nums
            extra = ''
        else:
            short = nums
            long = letters
            extra = letters[-1]
        
        temp = ''
        
        for i, j in zip(long, short):
            temp += i
            temp += j
            
        out = temp + extra
        
        return out