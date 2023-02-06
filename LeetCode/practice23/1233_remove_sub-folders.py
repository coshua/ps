class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        len_id = []
        for i in range(len(folder)):
            len_id.append((len(folder[i].split("/")), i))
        
        len_id.sort()
        defaultfolder = set()

        for cur in len_id:
            lst = folder[cur[1]].split("/")
            isSub = False
            for i in range(len(lst)):
                if '/'.join(lst[0:i]) in defaultfolder:
                    isSub = True
                    break
            if not isSub:
                defaultfolder.add('/'.join(lst))
        
        return list(defaultfolder)
