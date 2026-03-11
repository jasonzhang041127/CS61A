def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    i = 2
    if(n == 1):
        return False
    else:
        while(i < n):
            if(n % i != 0):
                i += 1
            else:
                return False
    return True
                
print(is_prime(10))
print(is_prime(7))
print(is_prime(1))