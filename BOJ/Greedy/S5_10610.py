n = input().strip()

indiv_sum = 0
cnt_zero = 0
for i in n:
    num = int(i)
    indiv_sum += num
    if num == 0:
        cnt_zero += 1

if indiv_sum % 3 == 0 and cnt_zero > 0:
    print(''.join(sorted(n, reverse=True)))
else:
    print(-1)