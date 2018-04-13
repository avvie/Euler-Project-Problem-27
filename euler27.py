from bisect import bisect_left
# sqrt(1000000000) = 31622


#Eratosthenous sieve algorithm from https://stackoverflow.com/questions/16004407/a-fast-prime-number-sieve-in-python
def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]



#primality test from https://stackoverflow.com/questions/4545114/quickly-determine-if-a-number-is-prime-in-python-for-numbers-1-billion

__primes = sieve_for_primes_to(31622)
def is_prime(n):
    # if prime is already in the list, just pick it
    if n <= 31622:
        i = bisect_left(__primes, n)
        return i != len(__primes) and __primes[i] == n
    # Divide by each known prime
    limit = int(n ** .5)
    for p in __primes:
        if p > limit: return True
        if n % p == 0: return False
    # fall back on trial division if n > 1 billion
    for f in range(31627, limit, 6): # 31627 is the next prime
        if n % f == 0 or n % (f + 4) == 0:
            return False
    return True

#primality test borrowed code ends here

def QuadFunc(n, a, b):
    return n**2 + a * n + b

maxChain = 0
n = 0
chain = 0

for a in range(-999, 1000, 1):
    for b in range(-1000, 1001, 1):
        
        n = 0
        result = QuadFunc(0,a,b)
        chain = 0

        while(is_prime(result)):
            chain = chain + 1 
            n = n + 1
            result = QuadFunc(n,a,b)

        if maxChain < chain:
            maxChain = chain
            print("a: " + str(a) + " \tb: " + str(b) + "\t chain: " + str(chain))


print(maxChain)


