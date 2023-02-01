#!/usr/bin/python3
import binascii
import sys

### Usage
### python3 toHex.py "jmp esp"

string_to_convert = sys.argv[1]
def reverse_string(string_to_convert):
    reversed = string_to_convert[::1]
    getReversed = [reversed[i:i+4] for i in range(0, len(reversed), 4)]

    return getReversed

def converter(string_to_convert):
    tobytes = string_to_convert.encode("utf-8")
    hexString = binascii.hexlify(tobytes).decode("utf-8")
    blocks = [hexString[i:i+8] for i in range(0, len(hexString), 8)]
    final_data = tuple(hex_block[6:8] + hex_block[4:6] + hex_block[2:4] + hex_block[0:2] for hex_block in blocks)

    return final_data
    
final_data = converter(string_to_convert)
ReversedStr = reverse_string(string_to_convert)
print("\nReversed String:",ReversedStr)
print("\nLittle-endian hexadecimal:\n")
for blocks in final_data[::-1]:
    print("0x"+blocks)

