"""
    Used for testing encryption and decryption using the Oeuf Cipher.
"""

from cipher import jEncrypt, jDecrypt


def getValid():
    textValid = False
    while not textValid:
        inText = str(input("Enter \'e\' for encryption or \'d\' for decryption: "))
        if (inText == "e") or (inText == "d"):
            textValid = True
    return inText


if __name__ == "__main__":
    inText = getValid()
    toEncrypt = str(input("Enter what to encrypt/decrypt: "))
    keyPhrase = str(input("Enter the key phrase: "))
    loopInt = int(input("Enter the looping integer: "))
    key = [keyPhrase, loopInt]
    res = jEncrypt(toEncrypt, key) if (inText == "e") else jDecrypt(toEncrypt, key)
    print(res)