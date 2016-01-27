# This contains multiple methods for generating primes.
# I use this for hackerrank coding challenges
def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n/3)
    for i in xrange(1,int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
        sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

def sieve(n):
    m = (n-1) // 2
    b = [True]*m
    i,p,ps = 0,3,[2]
    while p*p < n:
        if b[i]:
            ps.append(p)
            j = 2*i*i + 6*i + 3
            while j < m:
                b[j] = False
                j = j + 2*i + 3
        i+=1; p+=2
    while i < m:
        if b[i]:
            ps.append(p)
        i+=1; p+=2
    return ps

from bisect import bisect_left
# sqrt(1000000000) = 31622
__primes = primes2(31622)
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
	
def sieve(A):
	primes = [1]*(A+1)
	primes[0] = 0
	primes[1] = 0
	sqrtN = int(A**0.5)
	for i in range(2,sqrtN+1):
		if primes[i] == 1:
			for j in range(i*i, A+1, i):
				primes[j] = 0
	ret = []
	for i in range(2,A+1):
		if primes[i] == 1:
			ret.append(i)
	return ret
	
def c(N):
    i = 0
    flag = 0
    primes = []
    while len(primes) != N:
        if i < 3:
            i += 1
        else:
            i += 2
        if is_prime(i):
            primes.append(i)
    return max(primes)
    
# Input
# First line contains the number of inputs
# Second and lines after that contains the numbers 

T = int(raw_input())
for i in range(0,T):
    N = int(raw_input())
    print c(N)
