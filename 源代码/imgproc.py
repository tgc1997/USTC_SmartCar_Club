# -*- coding: utf-8 -*-

'向外提供两个有用的方法 \
imgproc.to_text(imagefile,textfile),将图片保存到textfile文件中 得到的textfile中只有01字符串 \
imgproc.to_img(textfile,imagefile),将textfile文件转换成RGB图片 要求textfile中有012字符串'
__author__='第十二届队员谭赣超'

import cv2
import numpy
from PIL import Image

class imgproc:
    def __init__(self,W=80,H=60):
        self.W=W
        self.H=H
        lw = [255] * 8 * 8 * 3
        lb = [0] * 8 * 8 * 3
        lr = [0,0,255] * 8 * 8
        lbr=[150,150,150]*640
        lbc=[150,150,150]*480
        lrr = [0, 0, 150] * 640
        lrc = [0, 0, 150] * 480
        self.imgw = numpy.array(lw).reshape(8, 8, 3)
        self.imgb = numpy.array(lb).reshape(8, 8, 3)
        self.imgr = numpy.array(lr).reshape(8, 8, 3)
        self.imgbr = numpy.array(lbr).reshape(1, 640, 3)
        self.imgbc = numpy.array(lbc).reshape(480, 1, 3)
        self.imgrr = numpy.array(lrr).reshape(1, 640, 3)
        self.imgrc = numpy.array(lrc).reshape(480, 1, 3)
        self.image = numpy.random.randint(0, 256, 480 * 640 * 3).reshape(480, 640, 3)
        self.W2 = self.image.shape[1]
        self.H2 = self.image.shape[0]

    def fill(self,line,y):
        for x in range(self.W):
            if int(line[x])==1:
                self.image[y * 8:(y + 1) * 8, x * 8:(x + 1) * 8] = self.imgw
            elif int(line[x])==2:
                self.image[y * 8:(y + 1) * 8, x * 8:(x + 1) * 8] = self.imgr
            else:
                self.image[y * 8:(y + 1) * 8, x * 8:(x + 1) * 8] = self.imgb

    def color(self,y,x):
        countw,countb=0,0
        for i in range(int(y*self.H1/self.H),int((y+1)*self.H1/self.H)):
            for j in range(int(x*self.W1/self.W),int((x+1)*self.W1/self.W)):
                if self.image1.item(i,j)==255:
                    countw+=1
                else:
                    countb+=1
        if countb>countw:
            return 0
        else:
            return 1

    def to_text(self,imagefile,textfile):
        image0=cv2.imdecode(numpy.fromfile(imagefile,dtype=numpy.uint8),-1)
        image0=cv2.cvtColor(image0,cv2.COLOR_RGB2GRAY)
        ret, image1 = cv2.threshold(image0, 127, 255, cv2.THRESH_BINARY)
        self.image1 = image1
        self.W1 = image1.shape[1]
        self.H1 = image1.shape[0]
        string= ''
        for y in range(self.H):
            for x in range(self.W):
                if self.color(y,x):
                    string+='1'
                else:
                    string+='0'
            string+='\n'
        with open(textfile, 'w') as f:
            f.write(string)
            f.close()

    def to_img(self,textfile,imagefile):
        with open(textfile,'r') as f:
            s=f.readlines()
            for i in range(self.H):
                self.fill(s[i].strip(),i)
        for x in range(self.W):
            self.image[0:480,x*8:x*8+1] = self.imgbc
        for y in range(self.H):
            self.image[y*8:y*8+1,0:640] = self.imgbr
        self.image[0:480, 320:321] = self.imgrc
        self.image[240:241, 0:640] = self.imgrr
        cv2.imwrite(imagefile, self.image)

if __name__=='__main__':
    img=imgproc()
    img.to_text(r'F:\picture\011A.jpg',r'F:\picture\011A.txt')
    img.to_img(r'F:\picture\011A.txt',r'F:\picture\011B.jpg')
    imgtest=Image.open(r'F:\picture\011B.jpg')
    imgtest.show()