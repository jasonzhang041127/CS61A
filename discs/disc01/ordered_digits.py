def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False
    """
    i = 0
    curr = 9
    while(x // pow(10, i) != 0):
        prev = curr
        curr = x // pow(10, i) % 10
        if(prev < curr):
            return False
        i += 1
    return True

print(ordered_digits(5))
print(ordered_digits(11))
print(ordered_digits(127))
print(ordered_digits(1357))
print(ordered_digits(21))
result = ordered_digits(1375)
print(result)