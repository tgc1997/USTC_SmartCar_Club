# -*- coding: utf-8 -*-
__author__='第十二届队员谭赣超'

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from imgproc import imgproc

class frame:
    def __init__(self):
        self.rt=Tk()
        self.rt.title('USTC Smartcar Club')
        im=Image.new('L',(640,480),255)
        photo = ImageTk.PhotoImage(im)
        self.labelimg = Label(image=photo)
        self.labelimg.image = photo
        self.labelimg.grid(row=1, column=0, columnspan=5, rowspan=30)
        self.label1=Label(self.rt,text='resolution 60*80')
        self.label1.config(font='Helvetica 10 ', fg='blue')
        self.label1.grid(row=0,column=0,sticky=W)
        self.button1=Button(self.rt,command=self.convert_all)
        self.button1.config(font='Helvetica 10 bold',bg='yellow',text='convert all',width=10,height=2)
        self.button1.grid(row=31,column=4)
        self.button2 = Button(self.rt, command=self.select)
        self.button2.config(font='Helvetica 10 bold', bg='yellow', text='select', width=6,height=2)
        self.button2.grid(row=31, column=1,sticky=E)
        self.button3 = Button(self.rt, command=self.toimage)
        self.button3.config(font='Helvetica 10 bold', bg='yellow', text='toimage', width=6,height=2)
        self.button3.grid(row=31, column=2,sticky=E)
        self.button4 = Button(self.rt, command=self.nextimage)
        self.button4.config(font='Helvetica 10 bold', bg='yellow', text='next', width=6, height=2)
        self.button4.grid(row=31, column=3, sticky=E)
        self.e3 = StringVar()
        self.e3.set('')
        self.entry3 = Entry(self.rt, textvariable=self.e3)
        self.entry3.config(font='Helvetica 13', width=40)
        self.entry3.grid(row=31, column=0)

    def convert_all(self):
        oname = filedialog.askopenfilename(filetypes=[('All Files','*')])
        picturedir=os.path.split(oname)[0]
        if not picturedir:
            return
        imglist=[x for x in os.listdir(picturedir) if os.path.isfile(os.path.join(picturedir,x)) and (os.path.splitext(x)[1] == '.jpg'
                                                                                        or os.path.splitext(x)[1] == '.jpeg'
                                                                                        or os.path.splitext(x)[1] == '.png')]
        imglistnew=self.rename(imglist,picturedir)
        image = imgproc()
        for img in imglistnew:
            imgfile1=os.path.join(picturedir,img)
            textfile1=os.path.join(picturedir,os.path.splitext(img)[0][0:-1]+'C.txt')
            if not os.path.exists(textfile1):
                image.to_text(imgfile1,textfile1)
            imgfile2=os.path.join(picturedir,os.path.splitext(img)[0][0:-1]+'B.jpg')
            textfile2=os.path.join(picturedir,os.path.splitext(img)[0][0:-1]+'D.txt')
            if os.path.exists(textfile2):
                image.to_img(textfile2,imgfile2)
            else:
                image.to_img(textfile1, imgfile2)

    def rename(self,imglist,picturedir):
        imglist1=list(filter(self.not_exsitb,imglist))
        imglistnew=[]
        for i in range(len(imglist1)):
            if i<10:
                s= '00' + str(i) + 'A.jpg'
            elif i<100:
                s= '0' + str(i) + 'A.jpg'
            else:
                s = str(i) + 'A.jpg'
            if not os.path.exists(os.path.join(picturedir,s)):
                os.rename(os.path.join(picturedir,imglist1[i]),os.path.join(picturedir,s))
            imglistnew.append(s)
        return imglistnew

    def not_exsitb(self,s):
        if (s[-4]=='.' and s[-5]=='B') or (s[-5]=='B' and s[-6]=='B'):
            return False
        else:
            return True

    def select(self):
        textname = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
        if  textname:
            self.e3.set(textname)

    def toimage(self):
        image=imgproc()
        if os.path.isfile(self.e3.get()) and self.e3.get()[-4:]=='.txt':
            image.to_img(self.e3.get(),self.e3.get()[0:-5]+'B.jpg')
            photo = ImageTk.PhotoImage(Image.open(self.e3.get()[0:-5]+'B.jpg'))
            self.labelimg = Label(image=photo)
            self.labelimg.image = photo
            self.labelimg.grid(row=1, column=0, columnspan=5, rowspan=30)
        elif self.e3.get()=='':
            messagebox.showinfo(message='please select a *.txt file !!!')
        else:
            messagebox.showinfo(message='not a *.txt file !!!')

    def nextimage(self):
        path=self.e3.get()
        if len(path)<8:
            return
        num=int(path[-8:-5])
        if num<9:
            s='00'+str(num+1)
        elif num<99:
            s='0'+str(num+1)
        else:
            s=str(num+1)
        self.e3.set(path[0:-8]+s+path[-5:])
        self.toimage()
        pass

if __name__ == "__main__":
    f=frame()
    f.rt.mainloop()
