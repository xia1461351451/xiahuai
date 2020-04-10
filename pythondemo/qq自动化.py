import random
import uiautomation
import time,os
from pykeyboard import PyKeyboard
from pynput.keyboard import Controller,Key
class GUI:
    def __init__(self):
        # 实例化键盘1对象
        self.keyboard=Controller()
        # 实例化鼠标1对象
        self.mose=Controller()
        # 程序运行位置
        self.path='C:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe'
        # 实例化键盘2对象
        self.k=PyKeyboard()
        # self.m=PyMouse()
    def loginQQ(self,qq,pwd):
        # 打开QQ
        os.popen(self.path)
        time.sleep(1)
        # 获取QQ窗口
        self.window=uiautomation.WindowControl(Name='QQ')
        time.sleep(1)
        # QQ输入框坐标
        self.window.Click(187,200)
        # 输入qq号
        self.keyboard.type(qq)
        time.sleep(1)
        # 密码输入框坐标
        # window.Click(187,240)
        # self.k.press_key(('BackSpace'))
        self.keyboard.press(Key.tab)
        # self.keyboard.release(Key.tab)
        time.sleep(1)
        # self.keyboard.type('19961214xiahuai')
        # 输入qq密码
        self.keyboard.type(pwd)
        self.window.Click(200,300)
        self.keyboard.release(Key.tab)
    def findqq(self,resuitqq):
        time.sleep(10)
        # 获取登录成功后的界面
        window1=uiautomation.WindowControl(name="QQ")
        # 定位搜素输入框，并点击
        window1.Click(123,110)
        # 粘贴输入框qq号码
        self.keyboard.type(resuitqq)
        # self.keyboard.type('1461351451')
        time.sleep(0.5)
        # 进入聊天界面
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
    def sendmesages(self,li):
        for i in range(1,10):
            self.keyboard.type(random.choice(li))
            self.keyboard.press(Key.enter)
            time.sleep(0.5)
            self.keyboard.release(Key.enter)
    def cellphone(self):
        pass
    def __del__(self):
        pass
if __name__ == '__main__':
    s = GUI()
    s.loginQQ('1461351451','xiahuai1996')
    li = ['这个世界就是这么神奇']
    s.findqq('1540092121')
    s.sendmesages(li)
