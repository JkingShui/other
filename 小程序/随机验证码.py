# -*- coding: utf-8 -*-

from captcha.image import ImageCaptcha
from random import randint
list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
chars = ''
for i in range(4):
    chars += list[randint(0, 62)] #随机从list中获取四个随机字符
image = ImageCaptcha().generate_image(chars) #将这个字符串绘制成图片

image.show() #显示出来