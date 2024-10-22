# Exploring Math with Python - Exercise 1-2

# a. Implement a Python function encodeModuloCipher as follows:
def encodeModuloCipher(strOrigMsg,validChars,denom):
    strEncode = ''
    for c in strOrigMsg:
        if c in validChars:
            i = validChars.index(c)
            c1 = i//denom
            c2 = i%denom
            s = str(c1)+str(c2)
            strEncode += s
    return strEncode

# b. Implement the function decodeModuloCipher as follows:
def decodeModuloCipher(strEncode,validChars,denom):
    strDecode = ''
    for i in range(0,len(strEncode),2):
        start = i
        c1 = int(strEncode[start])
        c2 = int(strEncode[start+1])
        c = c1*denom+c2
        v = validChars[c]
        strDecode += v
    return strDecode
        
# c. Implement main function
def main():
    cList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = "MATH RULES"
    en = encodeModuloCipher(code,cList,7)
    print(en)
    de = decodeModuloCipher(en,cList,7)
    print(de)
    
    cList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!:;'
    code = "Two plus two equals 4!"
    en = encodeModuloCipher(code,cList,9)
    print(en)
    de = decodeModuloCipher(en,cList,9)
    print(de)

main()
          
# ***** Console Output
# 150025102326140424
# MATHRULES
# 21534468454151486850534468334651284148686272
# Two plus two equals 4!
