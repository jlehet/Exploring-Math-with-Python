# imageProcessing

from PIL import Image

origfilename = "thinker"
filename = origfilename+".png"
inputImage = Image.open(filename).convert('RGB')
outputImage = Image.open(filename).convert('RGB')
outfilename = origfilename+"Copy"+".png"

(width,height) = inputImage.size

print("processing image: %d by %d pixels" % (width,height))

k = 0
for x in range(width):
    for y in range(height):
        (r,g,b) = inputImage.getpixel((x,y))        

        pixel = (r,g,b)
        outputImage.putpixel((x,y), pixel)

outputImage.save(outfilename, format="PNG")
outputImage.show()

