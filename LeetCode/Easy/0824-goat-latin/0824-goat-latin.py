class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        lst = sentence.split(" ")
        suf = ["a"]
        for i in range(len(lst)):
            word = lst[i]
            if word[0].lower() not in 'aeiou':
                word = word[1:] + word[0]

            word += "ma" + ''.join(suf)
            suf.append("a")
            lst[i] = word
        return " ".join(lst)