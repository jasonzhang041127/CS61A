def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    i = 0
    count = 0
    while(i <= 9):
        if(has_digit(n, i)):
            count += 1
        i += 1
    print(count)

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10, "k must be between 0 and 10"
    i = 0
    while(n // pow(10, i) != 0):
        curr = n // pow(10, i) % 10
        if(curr == k):
            return True
        i += 1
    return False

unique_digits(8675309)
unique_digits(13173131)
unique_digits(101)