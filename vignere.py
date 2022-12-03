from alphabet import alphabet

def getRepeatedKey(text, key):
    repeatedKey = ""
        
    for i in range(len(text)):
        repeatedKey += key[i%len(key)]
    
    return repeatedKey

def encrypt(plain, key):
    repeatedKey = getRepeatedKey(plain, key)
    cipher = ""

    for i in range(len(plain)):
        cipher += alphabet[(alphabet.index(plain[i]) + alphabet.index(repeatedKey[i]))%26]
        
    return cipher

def decrypt(cipher, key):
    repeatedKey = getRepeatedKey(cipher, key)
    plain = ""
        
    for i in range(len(cipher)):
        plain += alphabet[(alphabet.index(cipher[i]) - alphabet.index(repeatedKey[i]))%26]
        
    return plain

if __name__ == "__main__":
    cipher = encrypt('goofyahh', 'abcde')
    print(cipher)
    print(decrypt(cipher, 'abcde'))
    
    