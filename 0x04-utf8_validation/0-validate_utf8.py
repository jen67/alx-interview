#!/usr/bin/python3

def validUTF8(data):
    # Number of bytes remaining in the current UTF-8 character
    remaining_bytes = 0
    
    # Masks to identify the type of byte
    one_byte_mask = 0b10000000      # 1-byte character check
    two_byte_mask = 0b11100000      # 2-byte character start
    three_byte_mask = 0b11110000    # 3-byte character start
    four_byte_mask = 0b11111000     # 4-byte character start
    continuation_mask = 0b11000000  # Continuation byte check
    
    for num in data:
        # Mask to get only the 8 least significant bits
        byte = num & 0xFF
        
        if remaining_bytes == 0:
            # Determine the number of bytes in the character based on the first byte
            if (byte & one_byte_mask) == 0:
                continue  # 1-byte character, no need to check further
            elif (byte & two_byte_mask) == 0b11000000:
                remaining_bytes = 1
            elif (byte & three_byte_mask) == 0b11100000:
                remaining_bytes = 2
            elif (byte & four_byte_mask) == 0b11110000:
                remaining_bytes = 3
            else:
                return False  # Invalid start of UTF-8 character
        else:
            # Check if the byte is a continuation byte (10xxxxxx)
            if (byte & continuation_mask) != 0b10000000:
                return False
            remaining_bytes -= 1
    
    return remaining_bytes == 0

