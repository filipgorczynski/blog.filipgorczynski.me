Title: Understanding colors
Date: 2022-03-10 07:09
Modified: 2022-03-10 07:09
Category: Life
Tags: #tech, #colors, #art
Slug: understanding-colors
Author: filipgorczynski
Status: draft
Cover: https://blog.filipgorczynski.me/images/post/2022/03/denise-jones-jj4x2mlEYQ0.jpg
meta_url: https://blog.filipgorczynski.me/2022/03/understanding-colors
Summary: 

## bits per channel

RED      GREEN    BLUE     ALPHA
________ ________ ________ ________

24 bit = RGB
32 bits = RGBA
24 bits (RGB) + 8 bits of alpha => 32 bits

2^8 => 256
1-256 / 0-255

8 bit/channel images are too limited to be used as a light source in 3D computer grahic or in a professional color correction process in photography.
HDRI (High Dynamic Range Image):  image format with the ability to store color information above 8 bits per channel or above standard RGB.
Examples of HDRI file formats are: HDR (HDRI), OpenEXR, JPG XR, >8 bits PNG, RAW files, >8 bits TIFF
Our screen devices will not be able to display HDRI images in it's true form.

## Tone mapping

sRGB
