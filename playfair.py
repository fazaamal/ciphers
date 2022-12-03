import numpy as np
from alphabet import alphabet

def getStringArray(plain: str):
    
    array = [plain[0]]
    for i in range(1,len(plain)):
        if(len(array[-1]) == 1):
            if(array[-1] == plain[i]):
                array[-1] += 'x' if array[-1] != 'x' else 'z' 
                array.append(plain[i])
            else:
                array[-1] += plain[i]
        else:
            array.append(plain[i])
    
    if(len(array[-1]) == 1):
        array[-1] += 'x' if array[-1] != 'x' else 'z' 
    
    return array 

def generateKeySquare(key):
    square = np.empty((5,5), dtype=str)
    letters = alphabet.replace('j','')
    for i in range(len(key)):
        square[int(i/5)][i%5] = key[i]
    
    for row in range(5):
        for col in range(5):
            if(square[row][col] == ''):
                while(np.any(square[:,:] == letters[0])):
                    letters = letters[1:]
                square[row][col] = letters[0]
                letters = letters[1:]
    
    return square
    
def encrypt(plain: str, keySquare: np.ndarray):
    stringArray = getStringArray(plain)
    cipher = ""
    
    for pair in stringArray:
        firstLetterLoc = [np.where(keySquare == pair[0])[0][0], np.where(keySquare == pair[0])[1][0]]
        secLetterLoc = [np.where(keySquare == pair[1])[0][0], np.where(keySquare == pair[1])[1][0]]
        if(firstLetterLoc[0] == secLetterLoc[0]):
            cipher += keySquare[firstLetterLoc[0]][(firstLetterLoc[1]+1)%5]
            cipher += keySquare[firstLetterLoc[0]][(secLetterLoc[1]+1)%5]
        elif(firstLetterLoc[1] == secLetterLoc[1]):
            cipher += keySquare[(firstLetterLoc[0]+1)%5][firstLetterLoc[1]]
            cipher += keySquare[(secLetterLoc[0]+1)%5][firstLetterLoc[1]]
        else:
            cipher += keySquare[firstLetterLoc[0]][secLetterLoc[1]]
            cipher += keySquare[secLetterLoc[0]][firstLetterLoc[1]]
    
    return cipher

def decrypt(cipher: str, keySquare: np.ndarray):
    stringArray = getStringArray(cipher)    
    cipher = ""
    
    for pair in stringArray:
        firstLetterLoc = [np.where(keySquare == pair[0])[0][0], np.where(keySquare == pair[0])[1][0]]
        secLetterLoc = [np.where(keySquare == pair[1])[0][0], np.where(keySquare == pair[1])[1][0]]
        if(firstLetterLoc[0] == secLetterLoc[0]):
            cipher += keySquare[firstLetterLoc[0]][(firstLetterLoc[1]-1)%5]
            cipher += keySquare[firstLetterLoc[0]][(secLetterLoc[1]-1)%5]
        elif(firstLetterLoc[1] == secLetterLoc[1]):
            cipher += keySquare[(firstLetterLoc[0]-1)%5][firstLetterLoc[1]]
            cipher += keySquare[(secLetterLoc[0]-1)%5][firstLetterLoc[1]]
        else:
            cipher += keySquare[firstLetterLoc[0]][secLetterLoc[1]]
            cipher += keySquare[secLetterLoc[0]][firstLetterLoc[1]]
    
    return cipher

if __name__ == "__main__":
    key = 'monarchy'
    plain = 'ilovecryptography'
    keySquare = generateKeySquare(key)
    cipher = encrypt(plain, keySquare)
    
    print(f"Plaintext: {plain}")
    print(f"Key square: \n{keySquare}")
    print(f"Encrypted: {cipher}")
    print(f"Decrypted: {decrypt(cipher, keySquare)}")
    