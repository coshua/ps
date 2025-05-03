class Solution:
    def countVowels(self, word: str) -> int:
        numOfVowels = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for i in range(len(word)):
            if word[i] in vowels:
                numOfVowels += (len(word) - i) * (i + 1)
        
        return numOfVowels