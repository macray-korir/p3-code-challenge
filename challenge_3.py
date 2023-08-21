def solve(word):
    vowels = 'aeiou'
    consonant_values = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1) if chr(i) not in vowels}
    
    max_value = 0
    current_value = 0
    
    for char in word:
        if char in consonant_values:
            current_value += consonant_values[char]
            max_value = max(max_value, current_value)  # Update the max value if current value is greater
        else:
            current_value = 0 
    
    return max_value  # Return the highest value of consonant substrings


# Examples
print(solve("zodiacs"))   
print(solve("strength"))  
