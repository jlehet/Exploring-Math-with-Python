# encodeMsgInPNG

from PIL import Image

letter = 'K'
inStr = input("enter single letter: ")
letter = inStr[0]
inFilePrefix = 'thinker'
inFile = inFilePrefix+".png"
inputImage = Image.open(inFile).convert('RGB')  # unmodified input image
outputImage = Image.open(inFile).convert('RGB') # used to store encoded image

(width,height) = inputImage.size

print("encoding message into %d by %d pixels" % (width,height))

bitList = []
c = ord(letter)
for j in range(8):
    oC = (c//128)%2     # pick off the top bit
    bitList.append(oC)
    c = c%128           # remove top bit
    c = c*2             # shift left 1 bit
bitList.append(0)       # append 0 for every third Blue

k = 0
for x in range(width):
    for y in range(height):
        (r,g,b) = inputImage.getpixel((x,y))
        if k < len(bitList) :
            r = (r//2)*2 + bitList[k]
            g = (g//2)*2 + bitList[k+1]
            b = (b//2)*2 + bitList[k+2]
        pixel = (r,g,b)
        outputImage.putpixel((x,y), pixel)
        k = k+3

outfilename = inFilePrefix+"Encode"+letter+".png"
outputImage.save(outfilename, format="PNG")
