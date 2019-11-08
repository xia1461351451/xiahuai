import os
import time

import requests
import re
import json
class Girl:
    def __init__(self):
        self.start_time= time.time()
        self.s=requests.session()
        self.count = int(input("选择你要爬取的页数,页数必须大于3，太少没意思:"))
        print('***************************准备创建Mypictures目录****************************')
        self.path = 'C:\\Mypictures'
        dirbool = os.path.exists(self.path)
        if dirbool == True:
            print('Mypictures文件夹已经存在')
        else:
            os.makedirs(self.path)
            print('Mypicturew文件夹创建成功')
        self.url1 = 'https://tuchong.com/rest/tags/%E7%A7%81%E6%88%BF/posts?page=1&count=20&order=weekly&before_timestamp='
        print('**********正在爬取，请耐心等候**********')
    def geturl(self):
        urls = []
        # 构建所有页数链接
        urs=[]
        for i in range(1,self.count):
            ss=f'https://tuchong.com/rest/tags/%E7%A7%81%E6%88%BF/posts?page={i}&count=20&order=weekly&before_timestamp='
            urs.append(ss)#所有页数的链接
            for i in urs:
                responce1=self.s.get(i).text.replace('\/','/').replace('http','https')
                # 每个页面的所有人数链接
                lenth=len(json.loads(responce1)['postList'])
                # print(lenth)
                for i in range(1,lenth):
                    # json转字典
                    text1=json.loads(responce1)['postList'][i-1]
                    # print(text1)
                    # 获取url
                    url2=text1['url'].replace('tuchong','photo.tuchong').split('/')[-3]
                    url2='https://tuchong.pstatp.com/'+url2+'/f/'
                    # print(url2)
                    # print(responce1)
                    imgs=re.findall('"img_id": (\d+)',json.dumps(text1))
                    # print(imgs)
                    for i in imgs:
                        url3=url2+str(i)+'.jpg'
                        urls.append(url3)
        return urls
    # 获取图片
    def getpicture(self):
        # url='https://tuchong.pstatp.com/1527969/f/539793919.jpg'
        urls=self.geturl()
        f=0
        for i in urls:
            try:
                f+=1
                responce=self.s.get(i).content
                self.writepicture(f,responce)
            except:
                pass
        # 写入图片
    def writepicture(self,b,responce):
        path=self.path
        with open(f'{path}\\{b}.jpg', 'wb')as f:
            f.write(responce)
            f.close()
    def __del__(self):
        print('**********************************************')
        self.end_time=time.time()
        use_time=self.end_time-self.start_time
        print(f"耗时 {use_time} 秒")
        print(f'图片爬取成功，已存入 {self.path} 目录下')
if __name__ == '__main__':
    g=Girl()
    g.getpicture()