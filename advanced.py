import math

def sqrt(x):
    """Return square root of x. Raises ValueError for negative x."""
    if x < 0:
        raise ValueError("sqrt of negative number")
    return math.sqrt(x)

def power(base, exponent):
    """Return base ** exponent"""
    return base ** exponent

def percentage(part, whole):
    """Return the percentage (part/whole * 100). Raises ZeroDivisionError if whole == 0"""
    if whole == 0:
        raise ZeroDivisionError("whole cannot be zero for percentage calculation")
    return (part / whole) * 100

# quick tests
if __name__ == "__main__":
    print("sqrt(9) =", sqrt(9))
    print("2^8 =", power(2, 8))
    print("percentage(2,5) =", percentage(2, 5))