class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        charCount = [0]*26
        charCount2 = [0]*26

        right = len(s1) - 1

        for i in range(len(s1)):
            charCount[ord(s2[i]) - ord('a')] += 1
            charCount2[ord(s1[i]) - ord('a')] += 1

        for left in range(0, len(s2) - len(s1) + 1):
            if charCount == charCount2:
                return True
            charCount[ord(s2[left]) - ord('a')] -= 1

            if right < len(s2) - 1:
                right += 1
                charCount[ord(s2[right]) - ord('a')] += 1

        return False

        