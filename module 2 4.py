numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    count = 0
    is_prime = True
    if i == 1:
        continue
    for j in range(1, i+1):
        if i % j == 0:
            #print(j)
            count += 1
            #print(count)
    if count < 3:
        primes.append(i)
    elif count >= 3:
        not_primes.append(i)
print('Primes:', primes)
print('Not Primes:', not_primes)





