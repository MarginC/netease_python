from PIL import Image
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type = int, default = 80)
parser.add_argument('--height', type = int, default = 80)

args = parser.parse_args()

IMG = args.file
OUTPUT = args.output
WIDTH = args.width
HEIGHT = args.height

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|"
	"()1{}[]?-_+~<>i!lI;:,\"^`'. ")
length = len(ascii_char)

def get_char(r, g, b, alpha = 256):
	if alpha == 0:
		return ' '
	gray = int(0.2126*r + 0.7152*g + 0.0722*b)
	
	unit = (256.0 + 1)/length
	return ascii_char[int(gray/unit)]

if __name__ == '__main__':
	im = Image.open(IMG)
	im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
	
	txt = ""
	
	for i in range(WIDTH):
		for j in range(HEIGHT):
			txt += get_char(*im.getpixel((j, i)))
		txt += '\r\n'

	print txt
	
	if OUTPUT:
		with open(OUTPUT, 'w') as f:
			f.write(txt)
	else:
		with open("output.txt", 'w') as f:
			f.write(txt)
