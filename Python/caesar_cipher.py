def caesar_cipher(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
        else:
            shifted_char = char
        result += shifted_char

    return result

plainText = input("Enter the plaintext : ")
key = int(input("Enter the key : "))
cipherText = caesar_cipher(plainText, key)

print("Plaintext :", plainText)
print("Ciphertext :", cipherText)