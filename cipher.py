import random as rand

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # len(alphabet) = 26
NMOD = len(ALPHABET)

def stripSpecials(m):
    mes = str()
    for n in m:
        if n.isalpha() : mes += n.lower()
    return mes

def let2num(listMessage):
    numbers = [ord(listMessage) - 97 for listMessage in listMessage]
    return numbers

def num2let(listNumbers):
    letters = [chr(listNumbers + 97) for listNumbers in listNumbers]
    return letters

# m = message, privkey = [n, k]. n = modifier, k = times to loop
def jEncrypt(m, key):
    m = str(m)
    keyMod = str(key[0])
    keyLoop = int(key[1])
    strippedM = stripSpecials(m)
    listM = list(strippedM)
    numM = let2num(listM)
    encM = []
    currentRotation = 0
    for num in numM:
        keyModInt = let2num(keyMod)
        for loop in range(1, keyLoop):
            num += (loop*keyModInt[currentRotation % len(keyModInt)])
            currentRotation += 1
        num %= NMOD
        encM.append(num)
    encNumM = num2let(encM)
    encrypted =  u''.join(map(str, encNumM))
    return encrypted.upper()

def jDecrypt(c, key):
    c = str(c)
    keyMod = str(key[0])
    keyLoop = int(key[1])
    strippedC = stripSpecials(c)
    listC = list(strippedC)
    numC = let2num(listC)
    decM = []
    currentRotation = 0
    for num in numC:
        keyModInt = let2num(keyMod)
        for loop in range(1, keyLoop):
            num -= (loop*keyModInt[currentRotation % len(keyModInt)])
            currentRotation += 1
        num %= NMOD
        decM.append(num)
    decNumC = num2let(decM)
    decrypted = u''.join(map(str, decNumC))
    return decrypted.lower()

if __name__ == "__main__":
    toEncrypt = str(input("Enter what to encrypt: "))
    keyPhrase = str(input("Enter the key phrase: "))
    loopInt = int(input("Enter the looping integer: "))
    res = jEncrypt(toEncrypt, [keyPhrase, loopInt])
    print (res)