#!/usr/bin/env python

# -*- coding:utf-8 -*-

from PIL import Image

def xorFun(x, y):

    return x^y   

def orFun(x, y):

    return x|y   

def andFun(x, y):

    return x&y

def loadImage(filename):

    img = Image.open(filename)

    width, height = img.size

    img = img.convert("RGB")

    pixel = img.load()

    return width, height, pixel   

def combineImage(file1, file2, file3, func):

    w1, h1, p1 = loadImage(file1)

    w2, h2, p2 = loadImage(file2)   

    width = min(w1, w2)

    height = min(h1, h2)

    img = Image.new("RGB", (width, height))

    pix = img.load()

    for y in xrange(0, height):

        for x in xrange(0, width):

            r1, g1, b1 = p1[x, y]

            r2, g2, b2 = p2[x, y]

      pix[x, y] = func(r1,r2), func(g1,g2), func(b1,b2)

    img.save(file3)

if __name__ == "__main__":

    combineImage("pic1.jpg", "pic2.jpg", "xor.jpg", xorFun)

    combineImage("pic1.jpg", "pic2.jpg", "or.jpg", orFun)

    combineImage("pic1.jpg", "pic2.jpg", "and.jpg", andFun)