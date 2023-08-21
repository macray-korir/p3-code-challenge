def convert_to_24_hour(hour, minute, period):
    if period == "am":
        if hour == 12:
            hour_24 = 0
        else:
            hour_24 = hour
    else:  # period is "pm"
        if hour == 12:
            hour_24 = 12
        else:
            hour_24 = hour + 12
    
    return f"{hour_24:02d}{minute:02d}"


# Test Challenge 1
print(convert_to_24_hour(8, 30, "am"))  # 0830
print(convert_to_24_hour(8, 30, "pm"))  # 2030
print(convert_to_24_hour(12, 0, "am")) # 0000