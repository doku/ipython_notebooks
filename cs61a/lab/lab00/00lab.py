import random
#import numpy
#import itertools

def twenty_sixteen():
    """Come up with the most creative expression that evaluates to 2016,
    using only numbers and the +, *, and - operators.

    >>> twenty_sixteen()
    2016
    """
    #return 2016
    
    numberOfTries = 10000
    samp = ["+", "*", "-"]+ list(map(str, range(10)))
    #print(list(map(str, range(10))))
    #print(samp)
    tries = ("".join([samp[random.randint(0,12)] for _ in range(random.randint(4,9)) ]) for _ in range(numberOfTries))
    #print(list(tries))

    for i in tries:
        try:
            #print(i)
            exec("f = " + i)
            #print(f)
            #if f == 2016:
            #    print(f, i)
        except:
            f = 0
            continue
        if f == 2016:
            #print(f, i)
            return i