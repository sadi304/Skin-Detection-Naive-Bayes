from PIL import Image
import os

def absoluteFilePaths(directory):
  filePaths = []
  for dirpath,_,filenames in os.walk(directory):
    for f in filenames:
      filePaths.append(os.path.abspath(os.path.join(dirpath, f))) 
  return filePaths

imagePaths = absoluteFilePaths("./data/image")
maskPaths = absoluteFilePaths("./data/mask")

skinPixelNumber = [[[0 for k in range(256)] for j in range(256)] for i in range(256)]
nonskinPixelNumber = [[[0 for k in range(256)] for j in range(256)] for i in range(256)]

for i in range(len(imagePaths)):
  im = Image.open(imagePaths[i])
  ms = Image.open(maskPaths[i])
  im = im.convert('RGB')
  ms = ms.convert('RGB')

  width, height = im.size

  for y in range(height):
    for x in range(width):
      red, green, blue = im.getpixel((x, y))
      maskRed, maskGreen, maskBlue = ms.getpixel((x, y))
      
      if(maskRed>250 and maskGreen>250 and maskBlue>250):
        skinPixelNumber[red][green][blue] += 1
      else:
        nonskinPixelNumber[red][green][blue] += 1
  print('image no: ' + str(i) + ' processed!')
  im.close()
  ms.close()

skinPixels = 0
nonSkinPixels = 0

for i in range(256):
  for j in range(256):
    for k in range(256):
      skinPixelNumber[i][j][k] += 1
      skinPixels += skinPixelNumber[i][j][k]
      nonskinPixelNumber[i][j][k] += 1
      nonSkinPixels += nonskinPixelNumber[i][j][k]
  print("^", end="")
probabilityOfSkin = skinPixels / (skinPixels + nonSkinPixels)
probability = 0

f = open("./noesis.sadi", 'w')
f.write("")
for i in range(256):
  for j in range(256):
    for k in range(256):
      probability = skinPixelNumber[i][j][k] * probabilityOfSkin / (skinPixelNumber[i][j][k] + nonskinPixelNumber[i][j][k])
      f.write(str(probability) + "\n")
  print("*", end="")

f.close()