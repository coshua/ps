def prime_list(n):
    sieve = [True] * (n + 1)

    m = int((n + 1) ** 0.5)

    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i] == True]


# inclusive
print(prime_list(10))
