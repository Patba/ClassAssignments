alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = '!?., '


def Vencrypt(message, keyword):
    decoded = ""
    keyword_final = ''
    pointer = 0
    for i in range(0, len(message)):
        if message[i] in punctuation:
            keyword_final += message[i]
        else:
            keyword_final += keyword[pointer]
            pointer = (pointer + 1)%len(keyword)
    for i in range(0, len(message)):
        if message[i] in punctuation:
            decoded += message[i]
        else:
            ln = alphabet.find(message[i]) + alphabet.find(keyword_final[i])
            decoded += alphabet[ln%26]

    return decoded


def Vdecryption(message, keyword):
    decoded = ""
    keyword_final = ''
    pointer = 0
    for i in range(0, len(message)):
        if message[i] in punctuation:
            keyword_final += message[i]
        else:
            keyword_final += keyword[pointer]
            pointer = (pointer + 1)%len(keyword)
    for i in range(0, len(message)):
        if message[i] in punctuation:
            decoded += message[i]
        else:
            ln = alphabet.find(message[i]) - alphabet.find(keyword_final[i])
            decoded += alphabet[ln % 26]

    return decoded