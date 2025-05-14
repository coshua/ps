class LogSystem:

    def __init__(self):
        self.q = [] # time, id

    def put(self, id: int, timestamp: str) -> None:
        num_qr = int(timestamp.replace(":", ""))
        bisect.insort(self.q, (num_qr, id))

    def query_update(eslf, query, lo, hi):
        tmp = str(int(query[lo:hi]) + 1)
        if len(tmp) == 1:
            tmp = "0" + tmp
        return tmp
    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        q_s, q_e = "", ""
        if granularity == "Year":
            q_s = start[:4] + ":00:00:00:00:00"
            q_e = str(int(end[:4]) + 1) + ":00:00:00:00:00"
        elif granularity == "Month":
            q_s = start[:7] + ":00:00:00:00"
            q_e = end[:5] + self.query_update(end, 5, 7) + ":00:00:00:00"
        elif granularity == "Day":
            q_s = start[:10] + ":00:00:00"
            q_e = end[:8] + self.query_update(end, 8, 10) + ":00:00:00"
        elif granularity == "Hour":
            q_s = start[:13] + ":00:00"
            q_e = end[:11] + self.query_update(end, 11, 13) + ":00:00"
        elif granularity == "Minute":
            q_s = start[:16] + ":00"
            q_e = end[:14] + self.query_update(end, 14, 16) + ":00"
        else:
            q_s = start[:]
            q_e = end[:17] + self.query_update(end, 17, 19)
        num_s, num_e = int(q_s.replace(":", "")), int(q_e.replace(":", ""))
        lo, hi = bisect.bisect_left(self.q, (num_s, 0)), bisect.bisect_left(self.q, (num_e,0))
        ans = []
        for i in range(lo, hi):
            ans.append(self.q[i][1])
        return ans

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)