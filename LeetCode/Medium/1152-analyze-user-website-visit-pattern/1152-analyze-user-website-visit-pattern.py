class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        pair = []
        webidx = 0
        wtoi = {}
        itow = {}
        sz = len(username)
        for i in range(sz):
            w = website[i]
            if w not in wtoi:
                wtoi[w] = webidx
                itow[webidx] = w
                webidx += 1
            # time, Joe, webidx
            pair.append((timestamp[i], username[i], wtoi[w]))
        
        pair.sort()
        hist = {}
        for _, user, w in pair:
            if user not in hist:
                hist[user] = [{} for _ in range(3)]
            for prev in hist[user][1]:
                a, b = prev
                num = hist[user][1][prev]

                tup = (a, b, w)
                if tup not in hist[user][2]:
                    hist[user][2][tup] = 0
                hist[user][2][tup] += 1
            #update length 1
            for prev in hist[user][0]:
                a = prev
                num = hist[user][0][prev]

                tup = (a, w)
                if tup not in hist[user][1]:
                    hist[user][1][tup] = 0
                hist[user][1][tup] += 1

            if w not in hist[user][0]:
                hist[user][0][w] = 0
            hist[user][0][w] += 1
        anscnt = 0
        ansseq = []
        sumdict = defaultdict(int)
        for user in hist:
            for tup in hist[user][2]:
                # sumdict[tup] += hist[user][2][tup]
                sumdict[tup] += 1
                if sumdict[tup] > anscnt:
                    anscnt = sumdict[tup]
                    ansseq = [tup]
                elif sumdict[tup] == anscnt:
                    ansseq.append(tup)
        
        for i in range(len(ansseq)):
            tup = ansseq[i]
            strtup = [itow[tup[0]], itow[tup[1]], itow[tup[2]]]
            ansseq[i] = strtup
        print(ansseq)
        return min(ansseq)


        