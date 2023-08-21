def positive_no(a, b, c):
    positive_count = 0
    
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    
    return positive_count == 2  # Check if exactly two numbers are positive

    # Test case
print(positive_no(2, 4, -3))  
print(positive_no(-4, 6, 8))  
