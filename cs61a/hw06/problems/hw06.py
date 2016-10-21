###########
# Mobiles #
###########

def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    #weight = total_weight(left) + total_weight(right)
    return tree(None, [left, right])

def new_mobile(weight, left,right):
    return tree(weight, [left, right])

def sides(m):
    """Select the sides of a mobile."""
    return branches(m)

def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])

def side_weight(s):
    k = end(s)
    if is_weight(k):
        return size(k)
    elif is_mobile(k):
        return root(k)
    
def length(s):
    """Select the length of a side."""
    return root(s)

def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    return branches(s)[0]

def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    return tree(size, [])

def size(w):
    """Select the size of a weight."""
    return root(w)

def is_weight(w):
    """Whether w is a weight, not a mobile."""
    return len(branches(w)) == 0

def is_side(s):
    return len(branches(s)) == 1

def is_mobile(m):
    return len(branches(m)) == 2

def torq(s):
    """the length of side times the total weight"""
    return length(s) * total_weight(end(s))

def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        return sum([total_weight(end(sides(m)[0])), total_weight(end(sides(m)[1])) ])  #sum([total_weight(end(s)) for s in sides(m)])

def balanced(m):
    """Return whether m is balanced.

    #>>> t, u, v = examples()
    #>>> balanced(t)
    #True
    #>>> balanced(v)
    #True
    #>>> w = mobile(side(3, t), side(2, u))
    #>>> balanced(w)
    #False
    >>> t, u, v = examples()
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    m = with_totals(m)
    #if is_weight(m):
    #    return False
    if is_weight(m):
        return True
    if is_mobile(m):
        sideA = sides(m)[0]
        sideB = sides(m)[1]
        return length(sideA) *size(end(sideA)) == length(sideB) * size(end(sideB)) and balanced(end(sideA)) and balanced(end(sideB))
    
    
def with_totals(m):
    """Return a mobile with total weights stored as the root of each mobile.

    >>> t, _, v = examples()
    >>> root(with_totals(t))
    3
    >>> print(root(t))                           # t should not change
    None
    >>> root(with_totals(v))
    9
    >>> [root(end(s)) for s in sides(with_totals(v))]
    [3, 6]
    >>> [root(end(s)) for s in sides(v)]         # v should not change
    [None, None]
    """
    if is_weight(m):
        return m
    if is_mobile(m):
        sideA_len, sideA = length(sides(m)[0]), with_totals(end(sides(m)[0]))
        sideB_len, sideB = length(sides(m)[1]), with_totals(end(sides(m)[1]))
        #roo = root(m)
        return new_mobile(root(sideA) + root(sideB) , side(sideA_len, sideA), side(sideB_len, sideB) )
        #roo[0] = root(sideA) + root(sideB)
        #return roo
    
    """
    t = []
    if is_mobile(m):
        for s in sides(m):
            t.append(with_totals(end(s)))
        return tree(total_weight(sides(m)[0]) + total_weight(sides(m)[1]) , t)
    if is_weight(m):
        return m
    """



############
# Mutation #
############

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    pass_attempts = []
    def withdraw(amount, pas):
        nonlocal balance
        if pas == password and len(pass_attempts) < 3:
            if amount > balance:
                return "Insufficient funds"
            balance = balance - amount
            return balance
        else:
            if len(pass_attempts) >= 3:
                return "Your account is locked. Attempts: " + str(pass_attempts)
            pass_attempts.append(pas)
            return "Incorrect password"
    return withdraw

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    def joint(amount, pas):
        if pas == new_password:
            return withdraw(amount, old_password)
        else:
            return withdraw(amount, pas)
    new_res = withdraw(0, old_password)
    if type(new_res) == str:
        return new_res
    return joint