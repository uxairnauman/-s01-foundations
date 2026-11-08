#!/usr/bin/env python3

def decode_caesar(text, shift):
    result = ""

    for char in text:
        if "A" <= char <= "Z":
            result += chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
        elif "a" <= char <= "z":
            result += chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
        else:
            result += char

    return result


ciphertext = input("Enter the shifted text: ")

for shift in range(1, 26):
    print(f"Shift {shift:2}: {decode_caesar(ciphertext, shift)}")
