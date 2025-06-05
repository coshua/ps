class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        pt1 = pt2 = 0
        
        num = ""
        while pt2 < len(abbr):
            if abbr[pt2].isalpha():
                if num:
                    sz = int(num)
                    num = ""
                    pt1 += sz
                if pt1 >= len(word) or word[pt1] != abbr[pt2]:
                    return False
                pt1 += 1
                pt2 += 1
            else:
                if not num and abbr[pt2] == '0':
                    return False
                num += abbr[pt2]
                pt2 += 1
        if num:
            sz = int(num)
            pt1 += sz
        return pt1 == len(word)