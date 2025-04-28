def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    if low <= n <= high:
        return True
    else:
        return False

  
if __name__ == '__main__':
     print(in_range(10, 1, 5)) 
     print(in_range(10, 1, 50))