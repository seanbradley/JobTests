# simple solution

rom sys import argv
from time import time

def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.add(i)
    return i


# alternative simple solution (requires isprime helper function)

def isprime(num):
    num*=1.0s
    for div in range(2,int(num**0.5)+1):
        if num/div==int(num/div):
            return False
    return True

for a in range(2,100):
    if isprime(a):
        print a


# historic solution

def historic(n):
    primes = set([2])
    i, p = 2, 0
    while True:
        if prime(i, primes):
            p += 1
            if p == n:
                return primes
        i += 1


# naive solution

def naive(n):
    from itertools import count, islice
    primes = (n for n in count(2) if all(n % d for d in range(2, n)))
    return islice(primes, 0, n)


# regex solution (requires isPrime helper function)

def isPrime(n):
    import re
    # see http://tinyurl.com/3dbhjv
    return re.match(r'^1?$|^(11+?)\1+$', '1' * n) == None

def regexp(n):
    import sys
    N = int(sys.argv[1]) # number of primes wanted (from command-line)
    M = 100              # upper-bound of search space
    l = list()           # result list

    while len(l) < N:
        l += filter(isPrime, range(M - 100, M)) # append prime element of [M - 100, M] to l
        M += 100                                # increment upper-bound

    return l[:N] # print result list limited to N elements


# compare times for naive, historic, and regex solutions

def dotime(func, n):
    print func.__name__
    start = time()
    print sorted(list(func(n)))
    print 'Time in seconds: ' + str(time() - start)

if __name__ == "__main__":
    for func in naive, historic, regexp:
        dotime(func, int(argv[1]))


# seive of eratosthenes

def sieveOfErat(end):
  if end < 2: return []

  #The array doesn't need to include even numbers
  lng = ((end/2)-1+end%2)

  # Create array and assume all numbers in array are prime
  sieve = [True]*(lng+1)

  # In the following code, you're going to see some funky
  # bit shifting and stuff, this is just transforming i and j
  # so that they represent the proper elements in the array.
  # The transforming is not optimal, and the number of
  # operations involved can be reduced.

  # Only go up to square root of the end
  for i in range(int(sqrt(end)) >> 1):

    # Skip numbers that aren’t marked as prime
    if not sieve[i]: continue

    # Unmark all multiples of i, starting at i**2
    for j in range( (i*(i + 3) << 1) + 3, lng, (i << 1) + 3):
      sieve[j] = False

  # Don't forget 2!
  primes = [2]

  # Gather all the primes into a list, leaving out the composite numbers
  primes.extend([(i << 1) + 3 for i in range(lng) if sieve[i]])

  return primes