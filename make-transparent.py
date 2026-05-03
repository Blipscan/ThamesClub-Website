from PIL import Image
import os

src = r"C:\Users\super\Documents\Projects\ThamesClubSite\deploy\images\above-below_01.jpg"
out = r"C:\Users\super\Documents\Projects\ThamesClubSite\deploy\images\above-below_01.png"

print("SRC EXISTS:", os.path.exists(src))

img = Image.open(src).convert("RGBA")
pixels = []

for r, g, b, a in img.getdata():
    if r > 220 and g > 220 and b > 220:
        pixels.append((255, 255, 255, 0))
    else:
        pixels.append((255, 255, 255, 255))

img.putdata(pixels)
img.save(out)

print("OUT EXISTS:", os.path.exists(out))
print(out)
