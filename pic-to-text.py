#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'JoeyYi'

'''
pic to text converter
'''

from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_name", help="img file name")
parser.add_argument("--max_size", help="max height/width", type=int, default=300)
# max_size 输出文字行宽
args = parser.parse_args()
img = args.file_name
size = args.max_size
ascii_char = list('@#$%&!*^~`')

def get_char(r, g, b, alpha=256):
	gray = (2126 * r + 7152 * g + 722 * b) / 10000
	if alpha == 0:
		return ' '
	else:
		i = int(gray / (alpha+1) * len(ascii_char))
		return ascii_char[i]

def main(img, max_size):
	im = Image.open(img)
	height = im.height
	width = im.width
	if max(height, width) > max_size:
		r = max_size / max(height, width)
		height = int(height * r)
		width = int(width * r)
		im = im.resize((height, width))
	height = im.height
	width = im.width

	txt = ''	
	for i in range(0,height,3):
		for j in range(width):
			txt+= get_char(*im.getpixel((j,i)))
		txt+= '\n'
	#print (txt)
	f = open('output.txt','w')
	f.write(txt)
	f.close()


if __name__ == '__main__':
	main(img,size)