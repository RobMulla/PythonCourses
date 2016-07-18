# EdX MITx.6.00.1x - Week 6

# Lecture 12
# genPrimes problem

"""Write a generator, genPrimes, that returns the sequence of
prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ..."""


def genPrimes():
    primes = [2]
    x = 2
    while True:
        print "is true"
        for p in primes:
            if (x % p) == 0:
                print "if statement true"
                print x
            else:
                yield x
                print "if statement false"
                primes.append(x)
                print "primes are: " + str(primes)
        x+= 1


prime = genPrimes()

for n in genPrimes():
    print n
