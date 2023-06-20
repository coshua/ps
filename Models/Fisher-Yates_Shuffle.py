import random
def shuffle(arr):
    for i in range(len(arr)):
        idx = random.randrange(i, len(arr))
        arr[i], arr[idx] = arr[idx], arr[i]