# Exploring Math with Python - Exercise 1-3

# Implement a CaesarCipher function to both encode and decode messages 
def CaesarCipher(strMsg,validChars,shift,encodeFlag):
    strOut = ''
    validLen = len(validChars)
    if not encodeFlag:
        shift = 0-shift
    for c in strMsg:
        if c in validChars:
            ind = (validChars.index(c) + shift) % validLen
            strOut += validChars[ind]
    return strOut

def main():
    cList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .,!'
    code = "MATH RULES"
    en = CaesarCipher(code,cList,12,True)
    print(en)
    de = CaesarCipher(en,cList,12,False)
    print(de)
    
    cList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!:;'
    code = "Two plus two equals 4!"
    en = CaesarCipher(code,cList,12,True)
    print(en)
    de = CaesarCipher(en,cList,12,False)
    print(de)
    return

main()

# ***** Console Output
# YMBTI!CXQA
# MATH RULES
# f80G1x64G580Gq26mx4GAJ
# Two plus two equals 4!
