import psutil
p = psutil.Process()
def u(message: str = 'current'):
    p = psutil.Process()    
    rss = p.memory_info().rss / 2 ** 20
    print(f"[{message}] memory usage: {rss: 10.5f} MB")


m = [[0 for i in range(10000)] for _ in range(100)]
u()

# new line from 1112
# new line from Ipad