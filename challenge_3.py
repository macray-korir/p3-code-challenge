def consonantsolver(randomstr):
    lettermap = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
       'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }

    count = 0  # Initialize count
    countlist = []  # Initialize countlist to store each substring's total value

    for i in randomstr:
        if i not in "aeiou":
            count += lettermap.get(i, 0)  # Add the value of i to count
        else:
            if count > 0:  # Only append to countlist if count > 0
                countlist.append(count)
                count = 0  # Reset count

    # After looping, there might still be a count value that needs to be appended
    if count > 0:
        countlist.append(count)

    print(countlist)
    return max(countlist, default=0)  # Return the maximum value or 0 if countlist is empty

# Test the function
print(consonantsolver("zodiacs"))  
print(consonantsolver("strength"))  