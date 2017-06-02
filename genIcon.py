from __future__ import print_function
from PIL import Image
from PIL import ImageFilter
import os,sys
if len(sys.argv)<=1:
    print('please input folder')
else:
    print(sys.argv[1])
im=Image.open("icon.png")
print(im.format, im.size, im.mode)
w=im.size[0]/2
h=im.size[1]/2
out=im.resize((w, h))
out=out.filter(ImageFilter.SMOOTH)
out.save('icon-512-1.png', "PNG")

out=im.resize((w, h),Image.BILINEAR)
#out=out.filter(ImageFilter.CONTOUR)
out.save('icon-512-2.png', "PNG")

out=im.resize((w, h),Image.BICUBIC)
out.save('icon-512-3.png', "PNG")

out=im.resize((w, h),Image.LANCZOS)
out.save('icon-512-4.png', "PNG")