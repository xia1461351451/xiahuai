# http://www.pslink.cn/S5/app4/102126
# 提交失败内容
# /html/body/div[1]/form/div/h1
# 提交成功内容
# /html/body/div/form/div[1]/h1
import random



import time
from pykeyboard import PyKeyboard
from selenium import webdriver
class Work:
    def __init__(self):
        self.wd = webdriver.Firefox(firefox_binary=r"C:\软件\firefox.exe",
                                    executable_path=r"C:\工具\Firefox_driver\geckodriver.exe")
        self.wd.implicitly_wait(10)
        self.wd.maximize_window()
        self.key = PyKeyboard()
        # 订单编号
        self.order_number=[
            114752372333
        ]
        # 金额
        self.money=[
            1000
        ]
        # 用户名
        self.name=[
            106291
        ]
        # 手机号
        self.phone_number=[
            18750597639284
        ]
        self.fail_order_number=[]
    def grt_url(self,phone_number,order_number,money,name):

        # (   web 部分代码  )
        # 重复检测网址是否能打开
        while True:
            self.wd.get("http://www.pslink.cn/S3/jd1/106291")
            if "京东" in self.wd.find_element_by_xpath('/html/body/div[1]/form/div[1]/h3').text:
                break
            else:
                time.sleep(4)
        # 用户名
        self.wd.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[3]/input').send_keys(name)
        time.sleep(0.5)
        # 手机号
        self.wd.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[4]/input').send_keys(phone_number)
        # 订单编号
        time.sleep(0.5)
        self.wd.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[5]/input').send_keys(order_number)
        # 金额
        time.sleep(0.5)
        self.wd.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[7]/input').send_keys(money)
        time.sleep(0.5)
        self.wd.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[8]/div/label[2]').click()
        js = "window.scrollTo(100,450);"
        self.wd.execute_script(js)
        time.sleep(0.7)
        # 提交订单
        self.wd.find_element_by_xpath('//*[@id="tg_submit_button"]').click()
        time.sleep(1)
    def start_work(self):
        a=len(self.phone_number)
        aa=0
        for i in range(a):
            while True:
                self.grt_url(self.phone_number[i], self.order_number[i], self.money[i], self.name[i])
                if self.wd.title=='PSLink':
                    time.sleep(3)
                else:
                    aa+=1
                    break
        print(f'此次一共提交了{aa}条数据')
if __name__ == '__main__':
    w=Work()
    w.start_work()
