def encrypt(text, offset):
    encoded = ""
    for i in range(len(text)):
        char = text[i]
        encoded += chr((ord(char) + offset - 97)%26+97)
    return encoded


def decrypt(text, offset):
    decoded = ""
    for i in range(len(text)):
        char = text[i]
        decoded += chr((ord(char) + offset - 97) % 26 + 97)
    return decoded