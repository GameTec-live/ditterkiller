from PIL import Image
import sys

file = sys.argv[1]
print(file)
img = Image.open(file)
img = img.convert("RGBA")
datas = img.getdata()
width, height = img.size

color = []

for y in range(height):
    for x in range(15):
        r, g, b, a = img.getpixel((y, x))
        color.append((r, g, b, a))
print(color)

newData = []
for item in datas:
    if item in color:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("output.png", "PNG")
