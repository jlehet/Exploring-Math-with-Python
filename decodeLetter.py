# decodeMsgInPNG

from PIL import Image

filename = input("enter .png file image name: ")
filename = filename+".png"

inputImage = Image.open(filename).convert('RGB')
(width,height) = inputImage.size

C = 0
for col in range(3):
    (r,g,b) = inputImage.getpixel((0,col))
    C = C*8 + (((r%2)*2)+(g%2))*2+(b%2)
C = C//2     # remove 3rd Blue
letter = chr(C)
            
print("\nletter = %s" % letter)
