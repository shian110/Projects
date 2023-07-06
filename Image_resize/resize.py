from PIL import Image
import glob
import os
from icrawler.builtin import BingImageCrawler
import time
# 拡張子.txtのファイルを取得する
    

path = '*'
i = 1
j=1
def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))
# ファイル名を一括で変更する
# txtファイルを取得する

flist = glob.glob(path)
li=[[file,os.path.getctime(file)] for file in flist]
li2=sorted(li,key=lambda x: x[1])
flist=[file[0] for file in li2]



for file in flist:
    if(file[-1]!="y" and file[-1]!="t"):
        im = Image.open(file)
        im_new = crop_max_square(im)
        if(file[-2]=="n"):
            im_new = im_new.convert('RGB')
        im_new.save(str(i+100)+'.jpg', quality=95)
        os.remove(file)
    i+=1
    
flist = glob.glob(path)
for file in flist:
    if(file[-1]!="y" and file[-1]!="t"):
        im = Image.open(file)
        im_new = im.resize((500,500))
        im_new.save(str(j)+'.jpg', quality=95)

        os.remove(file)
    j+=1
