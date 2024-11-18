from PIL import Image


COLORS = [0, 85, 170, 255]

screen = Image.new('RGBA', (160, 144), 255)


with open('fb.bin', 'rb') as fp:
    fb = fp.read()

for x in range(160):
    for y in range(144):
        screen.putpixel((x, y), (fb[(y * 160 + x) * 4], fb[(y * 160 + x) * 4 + 1], fb[(y * 160 + x) * 4 + 2], fb[(y * 160 + x) * 4 + 3]))

screen.save('screen.png')
