# -*- coding:utf-8 -*-
import tkinter
from sys import argv
import fd
import fc
import ft
import fr
import multiprocessing
import os.path
from shutil import rmtree
from ctypes import windll
import os
import gc
from multiprocessing import Process

if __name__ == '__main__':
    multiprocessing.freeze_support()


def open_fdwin():
    if len(argv) != 1:
        print("Usage:%s camera_id\r\n" % (argv[0]))
    else:
        fd.CatchUsbVideo('Face Detection Example Program', 0)


def open_frwin(mname):
    if len(argv) != 1:
        print("Usage:%s camera_id\r\n" % (argv[0]))
    else:
        a1 = 0
        for ch1 in mname:
            if '\u4e00' <= ch1 <= '\u9fff':
                a1 = 1
                break
        if a1 == 1:
            windll.user32.MessageBoxA(0, u"主要人物名字不能有中文哦.^ _ ^".encode('gb2312'), u' 提示'
                                      .encode('gb2312'), 0)
        else:
            if os.path.exists('./temp/FaceModel/' + mname + '.face.model.h5'):
                fr.facerec(mname)
            else:
                windll.user32.MessageBoxA(0, u"请填写主要人物名字，并且进行识别之前请先对主要人物面部照片进行训练哦"
                                             u"^ _ ^".encode('gb2312'),u' 提示'.encode('gb2312'), 0)


def open_fcwin():
    if len(argv) != 1:
        print("Usage:%s camera_id\r\n" % (argv[0]))
    else:

        na = tkinter.Tk()
        na.title('Name Please')
        na.geometry("255x105+700+200")
        na.resizable(width=False, height=False)
        entry1 = tkinter.Entry(na)  # show="*" 可以表示输入密码
        entry1.grid(row=0, column=0, sticky='N', padx=6, pady=6)

        def fcwin(name):
            a1 = 0
            for ch1 in name:
                if '\u4e00' <= ch1 <= '\u9fff':
                    a1 = 1
                    break
            if a1 == 1:
                windll.user32.MessageBoxA(0, u"主要人物名字不能有中文哦.^ _ ^".encode('gb2312'), u' 提示'
                                          .encode('gb2312'), 0)
            else:
                if len(name) != 0:
                    fc.CatchPICFromVideo("Face Picture Collecting...", 0, 1200, './temp/FacePicCollect/' + name)

        button1 = tkinter.Button(na, text="确定", command=lambda: fcwin(entry1.get()), width=14, height=3)
        button1.grid(row=1, column=0, sticky='N', padx=6, pady=6)
        na.mainloop()


def func_clean():
    if os.path.exists('./temp'):  # 如果文件存在
        # 重建文件夹
        rmtree('./temp')
    os.makedirs('./temp/FacePicCollect')
    os.makedirs('./temp/FaceModel')


def open_ftwin(mname):
    if len(argv) != 1:
        print("Usage:%s camera_id\r\n" % (argv[0]))
    else:
        a1 = 0
        for ch1 in mname:
            if '\u4e00' <= ch1 <= '\u9fff':
                a1 = 1
                break
        if a1 == 1:
            windll.user32.MessageBoxA(0, u"主要人物名字不能有中文哦.^ _ ^".encode('gb2312'), u' 提示'
                                      .encode('gb2312'), 0)
        else:
            if os.path.exists('./temp/FacePicCollect/' + mname) and len(mname) != 0:
                p1 = Process(target=ft.begintraining(mname), args=('test',))
                p1.start()
                p1.join()
                gc.collect()
            else:
                windll.user32.MessageBoxA(0, u"请填写主要人物名字，并且进行训练之前请先收集包含主要人物在内的至少两个人的面部照片哦.^ _ ^".encode('gb2312'),
                                          u' 提示'.encode('gb2312'), 0)


def createwin():
    win = tkinter.Tk()
    # 设置标题
    win.title('Face Recognition (by LiJiaqi)')
    # 设置大小和位置
    win.geometry("355x335+600+200")
    # 设置窗口是否可变长、宽，True：可变，False：不可变
    win.resizable(width=False, height=False)
    str1 = os.getcwd()
    a = 0
    for ch in str1:
        if '\u4e00' <= ch <= '\u9fff':
            a = 1
            break
    if a == 0:
        # 创建按钮
        label = tkinter.Label(win,
                              text="Main Person\'s Name:",
                              font=("黑体", 10),
                              width=22,
                              height=2,
                              wraplength=180,
                              justify="left",
                              anchor="e")
        label.grid(row=0, column=0, sticky='W', padx=6, pady=6)
        entry2 = tkinter.Entry(win)  # show="*" 可以表示输入密码
        entry2.grid(row=0, column=1, sticky='W', padx=6, pady=6)
        button1 = tkinter.Button(win, text="人脸检测", command=open_fdwin, width=22, height=4)
        button1.grid(row=1, column=0, sticky='W', padx=6, pady=6)
        button2 = tkinter.Button(win, text="人脸采集", command=open_fcwin, width=22, height=4)
        button2.grid(row=2, column=0, sticky='W', padx=6, pady=6)
        button3 = tkinter.Button(win, text="人脸训练", command=lambda: open_ftwin(entry2.get()), width=22, height=4)
        button3.grid(row=2, column=1, sticky='W', padx=6, pady=6)
        button4 = tkinter.Button(win, text="人脸识别", command=lambda: open_frwin(entry2.get()), width=22, height=4)
        button4.grid(row=1, column=1, sticky='W', padx=6, pady=6)
        button5 = tkinter.Button(win, text="退出", command=win.quit, width=22, height=4)
        button5.grid(row=3, column=0, sticky='W', padx=6, pady=6)
        button6 = tkinter.Button(win, text="清除人脸数据", command=func_clean, width=22, height=4)
        button6.grid(row=3, column=1, sticky='W', padx=6, pady=6)
    else:
        label = tkinter.Label(win,
                              text="当前软件路径：",
                              font=("黑体", 10),
                              width=40,
                              height=2,
                              wraplength=300,
                              justify="left",
                              anchor="w")
        label.grid(row=0, column=0, sticky='W', padx=8, pady=8)
        label2 = tkinter.Label(win,
                              text=str1,
                              font=("黑体", 10),
                              width=45,
                              height=2,
                              wraplength=300,
                              justify="left",
                              anchor="center")
        label2.grid(row=1, column=0, sticky='W', padx=8, pady=8)
        label2 = tkinter.Label(win,
                              text="请将程序文件和haarcascades文件夹放于全英文路径下的同一文件夹内哦",
                              font=("黑体", 10),
                              width=47,
                              height=3,
                              wraplength=300,
                              justify="center",
                              anchor="center")
        label2.grid(row=2, column=0, sticky='W', padx=8, pady=8)
        button1 = tkinter.Button(win, text="明白了，我将手动转移以上两个文件到全英文路径下", command=win.quit, width=40, height=3)
        button1.grid(row=3, column=0, sticky='w', padx=24, pady=24)
    # 进入消息循环
    win.mainloop()


createwin()
