def checkPrime(n,primes):
    for prime in primes:
        if n % prime == 0:
            return False
    return True

def primesGen(n):
    primes = [2]
    for i in range(3,n,2):
        if checkPrime(i,primes):
            primes.append(i)
    return primes

a1 = 824694
a2 = 500
primes = primesGen(a1)

sums = 1
for i in range(a2):
    sums += primes[i]
    if sums in primes:
        print(primes[i],sums,primes.index(sums)+1)
    else:
        print(primes[i],sums)
