Title: Python i PIL - modyfikowanie obrazków
Date: 2019-04-25 13:48
Author: filipgorczynski
Category: Programowanie
Slug: python-i-pil-modyfikowanie-obrazkow
Status: draft

[![python](https://filipgorczynski.files.wordpress.com/2015/04/python1.png){.alignleft .wp-image-1002 .size-full width="128" height="128"}](https://filipgorczynski.files.wordpress.com/2015/04/python1.png)

from PIL import Image as PilImage

Obracanie obrazka

in\_file = 'c:\\\\dev\\\\tmp\\\\pylogo.png'  
out\_file = 'c:\\\\dev\\\\tmp\\\\pylogo2.png'  
im = PilImage.open(in\_file)  
rotated\_image = im.rotate(123)  
rotated\_image.save(out\_file)
