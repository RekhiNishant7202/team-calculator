def add(a, b):
    """Return a + b"""
    return a + b

def subtract(a, b):
    """Return a - b"""
    return a - b

def multiply(a, b):
    """Return a * b"""
    return a * b

def divide(a, b):
    """Return a / b. Raises ZeroDivisionError if b == 0"""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

# simple quick test when run directly
if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("4 * 6 =", multiply(4, 6))
    print("8 / 2 =", divide(8, 2))