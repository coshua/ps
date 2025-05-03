# 문자열 잘라서 뒤집기
s = "1234567890"
m = list(map(int, s))
print(m[len(s) - 1 :: -1])
