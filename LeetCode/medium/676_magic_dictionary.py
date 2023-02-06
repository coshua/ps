class MagicDictionary:

    def __init__(self):
        self.d = set()

    def buildDict(self, dictionary: list[str]) -> None:
        self.d = set(dictionary)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            for j in range(26):
                if ord(searchWord[i]) - ord('a') == j:
                    continue

                if searchWord[:i] + chr(j + ord('a')) + searchWord[i + 1:] in self.d:
                    return True

        return False