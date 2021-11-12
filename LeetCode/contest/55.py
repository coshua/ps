from sortedcontainers import SortedList
from collections import defaultdict
class MovieRentingSystem:

    def __init__(self, n: int, entries: list[list[int]]):
        # {movie: (price, shop)}
        self.shops = defaultdict(SortedList)
        
        # (price, shop, movie)
        self.rented = SortedList()

        # {(shop, movie): price}
        self.shop_movie = dict()

        for shop, movie, price in entries:
            self.shops[movie].add((price, shop))
            self.shop_movie[(shop, movie)] = price

    def search(self, movie: int) -> list[int]:
        return [y for _,y in self.shops[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_movie[(shop, movie)]
        self.shops[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.shop_movie[(shop, movie)]
        self.shops[movie].add((price, shop))
        self.rented.remove((price, shop, movie))

    def report(self) -> list[list[int]]:
        return [[y, z] for _,y,z in self.rented[:5]]

if __name__ == "__main__":
    s = MovieRentingSystem(10,[[4,374,55],[1,6371,21],[8,3660,24],[1,56,32],[5,374,71],[3,4408,36],[6,9322,73],[6,9574,92],[8,7834,62],[2,6084,27],[7,3262,89],[2,8959,53],[0,3323,41],[6,6565,45],[0,4239,20]])
    s.rent(0, 4239)
    s.drop(0, 4239)
    s.rent(3, 4408)
    s.rent(2, 6084)
    s.rent(0, 4239)
    s.drop(0, 4239)
    print(s.search(9346))
    print(s.report())
    s.rent(6, 9322)
    print(s.search(8698))