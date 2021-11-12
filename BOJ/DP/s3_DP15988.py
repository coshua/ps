time = [0] * 1000001
time[0] = 1
time[1] = 1
time[2] = 2
for i in range(3, 1000001):
    time[i] = (time[i - 1] + time[i - 2] + time[i - 3])
    time[i] % 1000000009

for _ in range(int(input())):
    print(time[int(input())])