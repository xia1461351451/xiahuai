# http://www.pslink.cn/S5/app4/102126
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
    def grt_url(self):
        self.wd.get("http://www.pslink.cn/S12/app3/104485")
        time.sleep(0.5)
        a=str(random.randint(0,9))
        b=str(random.randint(0,9))
        c=str(random.randint(0,9))
        d=str(random.randint(0,9))
        e=str(random.randint(0,9))
        phone_number ="181901" + a+b+c+d+e
        print(phone_number)
        # 手机号
        self.wd.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[2]/input').send_keys(phone_number)
        # 订单编号
        self.wd.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[3]/input').send_keys("E"+c+d+"H"+a+b+e)
        # 金额
        self.wd.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[5]/input').send_keys('1')
        self.wd.find_element_by_xpath('/html/body/div[1]/form/div[2]/div[6]/div/label[2]').click()
        js = "window.scrollTo(100,450);"
        self.wd.execute_script(js)
        time.sleep(0.3)
        self.wd.find_element_by_xpath('//*[@id="tg_submit_button"]').click()

if __name__ == '__main__':
    w=Work()
    for i in range(20):
        w.grt_url()
        i+=1
        time.sleep(1)