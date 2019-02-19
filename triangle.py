def search(a,b,t):
    """
    (int, int, int) -> int
    This program returns a basic side of triangle through the usage of the binary search.
    >>> search(10, 12, 0.9)
    4.875
    """
    lower = 0
    upper = b
    h = (a ** 2 - (b / 2) ** 2) ** 0.5
    while True:
        l = (lower + upper) / 2
        if abs(l**2 - square(l,a,h,b)) < t:
            return l
        elif (l**2 - square(l,a,h,b)) < 0:
            lower = l
        elif (l**2 - square(l,a,h,b)) > 0:
            upper = l
def square(l,a,h,b):
    return ((1/2*b*h) - ((h - l) * l / 2 + (b - l) * l / 2))
if __name__ == "__main__":
    import doctest
    doctest.testmod()
a, b, t = map(float,input().strip().split())
print(search(a,b,t))

