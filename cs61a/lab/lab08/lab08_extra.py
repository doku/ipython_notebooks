def make_advanced_counter_maker():
    """Makes a function that makes counters that understands the
    messages "count", "global-count", "reset", and "global-reset".
    See the examples below:

    >>> make_counter = make_advanced_counter_maker()
    >>> tom_counter = make_counter()
    >>> tom_counter('count')
    1
    >>> tom_counter('count')
    2
    >>> tom_counter('global-count')
    1
    >>> jon_counter = make_counter()
    >>> jon_counter('global-count')
    2
    >>> jon_counter('count')
    1
    >>> jon_counter('reset')
    >>> jon_counter('count')
    1
    >>> tom_counter('count')
    3
    >>> jon_counter('global-count')
    3
    >>> jon_counter('global-reset')
    >>> tom_counter('global-count')
    1
    """
    global_count = 0

    def global_counter():
        nonlocal global_count
        local_count = 0
        
        def local_counter(ty):
            nonlocal local_count 
            nonlocal global_count
            if ty == "global-count":
                global_count = global_count + 1
                return global_count
            elif ty == "global-reset":
                global_count = 0
                #return global_count
            elif ty == "count":
                local_count = local_count + 1
                return local_count
            elif ty == "reset":
                local_count = 0
                #return local_count
        return local_counter
    return global_counter



def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'No deal!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    """
    m, n = 1, 1
    f_sum, s_sum = first[0], second[0]
    f_len, s_len = len(first), len(second)
    #def helper(first, second, m, n):
    while f_sum != s_sum and m < f_len and n < s_len:
        #print(m, n, f_sum, s_sum)
        if f_sum > s_sum:
            n += 1
            s_sum += second[n-1]
        if f_sum < s_sum:
            m += 1
            f_sum += first[m-1]            
    if f_sum == s_sum: # change this line!
        first[:m], second[:n] = second[:n], first[:m]
        return 'Deal!'
    else:
        return 'No deal!'

def boom(n):
    sum = 0
    a, b = 1, 1
    while a <= n*n:
        while b <= n*n:
            sum += (a*b)
            b += 1
        b = 0
        a += 1
    return sum
