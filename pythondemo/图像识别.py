import random
from PIL import ImageGrab,Image
import time
class Match_picture:
    def __init__(self):
        time.sleep(5)
        # pass
    def find_img(self,path):
        big1=ImageGrab.grab() #获取屏幕对象
        # 获取坐标RGB颜色对象
        big2=big1.convert('RGBA').load()
        # print(big2[0,0])
        # 获取屏幕的尺寸
        big3=big1.size
        # print(big3)

        # 小图对象
        small1=Image.open(path)
        # 获取模板图（小图）RGB色对象
        small2=small1.convert('RGBA').load()
        # print(small2[0,0])
        # 获取模板图片尺寸
        small3=small1.size
        # print(small3)
        # 每一个像素点移动
        for x in range(big1.width-small1.width):
            for y in range(big1.height-small1.height):
                # 随机挑选小图的位置，进行粗略匹配
                lists = self.random_posizetion(small1)
                for i in lists:
                    # 如果随机选取的位置RGB色相同，再进行完全匹配
                    if big2[x + i[0], y + i[1]] == small2[i[0], i[1]]:
                        # 进行完全匹配，如果匹配度大于70%，返回True，如果小于70%，返回False
                        if self.check_math(big2, x, y, small1, small2):
                            print(f'定位成功，坐标为{x + int(small1.width / 2), y + int(small1.height / 2)}')
                            # 计算匹配位置的最中心位置
                            return (x + int(small1.width / 2), y + int(small1.height / 2))
        return (-1, -1)
    def random_posizetion(self,small):
        num= random.randint(5,10)
        lists=[]
        for i in range(num):
            x= random.randrange(small.width)
            y=random.randrange(small.height)
            lists.append([x,y])
        return lists
    # 对图片进行相似度计算
    def check_math(self,bdata,x,y,small,sdata):
        same=0
        diff=0
        for i in range(small.width):
            for j in range(small.height):
                if bdata[x+i,y+j]==sdata[i,j]:
                    same+=1
                else:
                    diff+=1
        simi = same / (same + diff)
        if simi > 0.7:
            return True
        else:
            return False
if __name__ == '__main__':
    a=Match_picture()
    path='C:\python-project\三阶段\图像识别/3.png'
    t=a.find_img(path)