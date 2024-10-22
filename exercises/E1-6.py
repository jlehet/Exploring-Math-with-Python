# Exploring Math with Python - Exercise 1-4

# Implement a VigenereCipher function to both encode and decode messages
def VigenereCipher(strOrigMsg, validChars, keyword, encodeFlag):
    strOut = ''
    validLen = len(validChars)
    keywordLen = len(keyword)
    outList = []
    for j in range(keywordLen):
        ordList = []
        shift = validChars.index(keyword[j])
        if not encodeFlag:
            shift = 0-shift
        for i in range(j,len(strOrigMsg),keywordLen):
            m = (validChars.index(strOrigMsg[i])+shift) % validLen
            ordList.append(m)
        outList.append(ordList)
    for i in range(len(outList[0])):
        for j in range(len(outList)):
            if len(outList[j]) > i:
                strOut += validChars[outList[j][i]]
    return strOut

def main():
    cList = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!:;'"
    print(len(cList))
    keywords = ["Math","Python","Keyword!"]
    en = 'SVPgQgrVWDQg8OGaA!!ZoaJ!zLmJEAIKCOPgrVWDQj'
    for keyword in keywords:
        print("keyword =",keyword)
        de = VigenereCipher (en,cList,keyword,False)
        print(de)
    return

main()

# ***** Console Output


