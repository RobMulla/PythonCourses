# EdX MITx.6.00.1x - Week 6

# Lecture 12
# genPrimes problem

"""Write a generator, genPrimes, that returns the sequence of
prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ..."""


def genPrimes():
    primes = []
    x = 1
    yield 2
    x += 1
    primes.append(x)
    while True:
        print "primes list is:  " + str(primes)
        for p in primes:
            if (x % p) == 0:
                x += 1
        yield x
        primes.append(x)
        x += 1



prime = genPrimes()

print str(prime.next()) + "    should be 2"
print str(prime.next()) + "    should be 3"
print str(prime.next()) + "    should be 5"
print str(prime.next()) + "    should be 7"
print str(prime.next()) + "    should be 11"
print str(prime.next()) + "    should be 13"
print str(prime.next()) + "    should be 17"
print str(prime.next()) + "    should be 19"


sdfasdf

