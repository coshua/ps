import bisect
class SnapshotArray:
    arr = None
    cnt = None

    def __init__(self, length: int):
        self.arr = [[[0, 0]] for i in range(length)]
        self.cnt = 0

    def set(self, index: int, val: int) -> None:
        if self.arr[index][-1][0] == self.cnt:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([self.cnt, val])

    def snap(self) -> int:
        self.cnt += 1
        return self.cnt - 1        

    def get(self, index: int, snap_id: int) -> int:
        ans = bisect.bisect_left(self.arr[index], snap_id, key=lambda i: i[0])
        if ans >= len(self.arr[index]):
            return self.arr[index][-1][1]
        elif self.arr[index][ans][0] > snap_id:
            return self.arr[index][ans - 1][1]
        else:
            return self.arr[index][ans][1]