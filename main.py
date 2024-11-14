from PIL import Image


COLORS = [0, 85, 170, 255]

screen = Image.new('L', (160, 144), 255)


with open('fb.bin', 'rb') as fp:
    fb = fp.read()

for x in range(160):
    for y in range(144):
        screen.putpixel((x, y), COLORS[fb[y * 160 + x]])

screen.save('screen.png')
