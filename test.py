from PIL import Image

ratio = [[[0 for k in range(256)] for j in range(256)] for i in range(256)]

with open("./noesis.sadi", "r") as file:
  for i in range(256):
    for j in range(256):
      for k in range(256):
        probability = file.readline()
        ratio[i][j][k] = float(probability)
print('data collected!')

image = Image.open("./data/test2.jpg")
im = image.convert('RGB')
width, height = im.size

im2 = Image.new(im.mode, im.size)

for y in range(height):
  for x in range(width):
    red, green, blue = im.getpixel((x, y))
    if(ratio[red][green][blue] > .15):
      im2.putpixel((x, y), (250, 250, 250))
    else:
      im2.putpixel((x, y), (0, 0, 0))
  print("*", end="")

im2.save("./detected.jpg")
        