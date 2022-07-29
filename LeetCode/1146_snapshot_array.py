import bisect
class SnapshotArray:
    arr = None
    cnt = None

    def __init__(self, length: int):
        self.arr = [[] for i in range(length)]
        self.cnt = 0

    def set(self, index: int, val: int) -> None:
        if self.arr[index] and self.arr[index][-1] == self.cnt:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([self.cnt, val])

    def snap(self) -> int:
        self.cnt += 1
        return self.cnt - 1        

    def get(self, index: int, snap_id: int) -> int:
        ans = bisect.bisect_left(self.arr[index], snap_id, key=lambda i: i[0])
        return ans[1]