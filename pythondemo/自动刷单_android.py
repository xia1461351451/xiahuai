# http://www.pslink.cn/S5/app4/102126
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
        self.order_number = [
            114752372330
        ]
        # 金额
        self.money = [
            1000
        ]
        # 用户名
        self.name = [
            106291
        ]
        # 手机号
        self.phone_number = [
            18750596075
        ]
        self.fail_order_number = []
    def grt_url(self,phone_number,order_number,money):

        # (   app安卓部分代码)

        while True:
            self.wd.get("http://www.pslink.cn/S3/jd1/106291")
            try:
                web_title = self.wd.find_element_by_xpath('/html/body/div[1]/form/div[1]/h3').text
                if "京东" in web_title:
                    print(web_title)
                    break
                else:
                    time.sleep(4)
            except Exception as f:
                continue
            else:
                print("网页正常打开")


        # 手机号
        self.wd.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[2]/input').send_keys(phone_number)
        # 订单编号
        time.sleep(0.3)
        self.wd.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[3]/input').send_keys(order_number)
        # 金额
        time.sleep(0.3)
        self.wd.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[5]/input').send_keys(money)
        time.sleep(0.3)
        self.wd.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[6]/div/label[2]').click()
        js = "window.scrollTo(100,450);"
        self.wd.execute_script(js)
        time.sleep(0.3)
        # 提交订单
        self.wd.find_element_by_xpath('//*[@id="tg_submit_button"]').click()
        time.sleep(1)

    def start_work(self):
        a = len(self.phone_number)
        aa = 0
        for i in range(a):
            while True:
                self.grt_url(self.phone_number[i], self.order_number[i], self.money[i])
                if self.wd.title == 'PSLink':
                    time.sleep(1)
                else:
                    aa += 1
                    break
        print(f'此次一共提交了{aa}条数据')
if __name__ == '__main__':
    w=Work()
    w.start_work()
