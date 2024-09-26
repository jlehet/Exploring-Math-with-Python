# encodeMsgInPNG

from PIL import Image

msg = input("enter message to encode: ")
msg = msg+"      " # append five blanks to the end of the message

# the following will convert each character in msg to a number
# using the ord function and then change this number into a
# binary string
bitList = []
for i in range(len(msg)):
    c = ord(msg[i])
    for j in range(8):
        oC = (c//128)%2     # pick off the top bit
        bitList.append(oC)
        c = c%128           # remove top bit
        c = c*2             # shift left 1 bit
    bitList.append(0)       # append 0 for every third Blue

filename = input("enter .png file image name: ")
filename = filename+".png"
inputImage = Image.open(filename).convert('RGB')
outputImage = Image.open(filename).convert('RGB')

(width,height) = inputImage.size

print("encoding message into %d by %d pixels" % (width,height))

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

outfilename = input("enter output .png file name: ")
outfilename = outfilename+".png"
outputImage.save(outfilename, format="PNG")
