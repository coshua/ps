class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        station = [[] for i in range(10**6 + 1)]
        for i in range(len(routes)):
            for stop in routes[i]:
                station[stop].append(i)
        if target == source:
            return 0
        v_s = set()
        v_bus = set()
        step = 1
        q, nq = [source], []
        while q:
            for s in q:
                while station[s]:
                    nxt_bus = station[s].pop()
                    if nxt_bus not in v_bus:
                        v_bus.add(nxt_bus)
                        for stop in routes[nxt_bus]:
                            if stop == target:
                                return step
                            if stop not in v_s:
                                v_s.add(stop)
                                nq.append(stop)
            q = nq
            nq = []
            step += 1
        return -1
