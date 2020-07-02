
import threading
import time
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import os
import re
from wsgiref.validate import validator

class Main:
    # 用户登录状态标识
    user_stste = False

# 登录界面：
class Login(Frame,Main):
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master
        self.root.geometry('900x450+100+50')
        self.root.title('九州CPE性能监控')
        self.creatwidget()
        self.root.mainloop()

    def creatwidget(self):
        # 用户名接收参数
        self.v1 = StringVar()
        # 密码接收参数
        self.v2 = StringVar()
        global photo
        # 用户名
        photo = PhotoImage(file='./1.gif')
        lable = Label(self.root, image=photo)
        lable.place(x=0, y=0)
        lable_user = Label(self.root, text='用户名：', font=('黑体', "16"))
        lable_user.place(x=450, y=100)
        entry1 = Entry(self.root, textvariable=self.v1)
        entry1.place(x=550, y=97, height=30)

        # 密码
        lable_password = Label(self.root, text='密  码：', font=('黑体', "16"))
        lable_password.place(x=450, y=150)
        entry2 = Entry(self.root, textvariable=self.v2, show='*')
        entry2.place(x=550, y=147, height=30)

        # 登录
        button_longin = Button(
            self.root,
            text='登 录',
            font=(
                '黑体',
                "16"),
            bg='white',
            command=self.check_password)
        button_longin.place(x=450, y=250)

        # 退出
        button_destory = Button(self.root, text='退出', font=(
            '黑体', "16"), bg='white', command=self.root.destroy)
        button_destory.place(x=600, y=250)

        button_clear1 = Button(
            self.root,
            text='清 除',
            font=(
                '黑体',
                "16"),
            bg='white',
            command=self.set_v1)
        button_clear1.place(x=750, y=95)

        button_clear2 = Button(
            self.root,
            text='清 除',
            font=(
                '黑体',
                "16"),
            bg='white',
            command=self.set_v2)
        button_clear2.place(x=750, y=145)

        button_support = Button(
            self.root,
            text='技术支持',
            font=(
                '黑体',
                "16"),
            bg='#FFC125',
            command=self.creat)
        button_support.pack(side=RIGHT, expand=YES, fill=NONE, anchor=SE)
    #     密码核对
    def check_password(self):
        user_name = '1'
        pass_word = '1'
        if self.v1.get() == user_name and self.v2.get() == pass_word:
            # 如果登录成功，修改用户状态标识
            Main.user_stste=True
            # 退出登录窗口
            self.root.destroy()
            # pass
        else:
            # 登录失败提示
            messagebox.showinfo('登录', '用户名或密码错误,请联系管理员：夏槐')
    # 清空用户名
    def set_v1(self):
        self.v1.set('')
    # 清空密码
    def set_v2(self):
        self.v2.set('')
    # 技术支持窗口
    def creat(self):
        global photo, photo1, top
        # # 用户名
        top = Toplevel()
        top.title('感谢技术支持')
        top.geometry('850x450+150+100')
        photo = PhotoImage(file='./zfb.png')
        lable1 = Label(top, image=photo)
        lable1.place(x=0, y=0)

        photo1 = PhotoImage(file='./wx.png')
        lable2 = Label(top, image=photo1)
        lable2.place(x=420, y=0)

        all_font = font.Font(family='宋体', size=20, weight=font.BOLD)
        retur = Button(top, text='返回', font=all_font, command=top.destroy)
        # retur = Button(top, text='返回', font=all_font)
        # retur.bind('<Button-1>',top.destroy)
        retur.place(x=425, y=410)

        Label(top, text='QQ:1461351451', font=20).place(x=30, y=430)


# 界面2
class Test_interface(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master
        self.root['background'] = '#C6E2FF'
        self.root.geometry('900x450+100+50')
        self.root.title('九州CPE性能监控')
        self.creatwidget()
        self.root.mainloop()

    def creatwidget(self):
        # 背景图片
        # global photo
        # # 用户名
        # photo = PhotoImage(file='./2.png')
        # lable = Label(self.root, image=photo)
        # lable.place(x=0,y=0)

        # adb检测
        adb = Button(
            self.root,
            command=self.check_network,
            font=15,
            bg='#87CEFF')
        adb['text'] = 'ADB环境检测'
        adb.place(x=10, y=10)

        # 日志显示区域
        self.log_data = Text(self.root, width=200, height=34, bg='#C6E2FF')
        self.log_data.place(x=450, y=0)
        # 日志区域滑块
        scroll=Scrollbar()
        scroll.pack(side=RIGHT, fill=Y)
        # 两个控件关联
        scroll.config(command=self.log_data.yview)
        self.log_data.config(yscrollcommand=scroll.set)
        # 当前apk包名
        package_name = Button(
            self.root,
            command=self.get_package,
            font=15,
            text='当前桌面apk包名',
            bg='#87CEFF')
        package_name.place(x=240, y=10)
        # 重启ADB
        package_name = Button(
            self.root,
            command=self.restart_adb,
            font=15,
            text='重启ADB',
            bg='#87CEFF')
        package_name.place(x=140, y=10)

        # adb连接测试
        self.v3 = StringVar()
        self.v3.set('10.6.252.236')
        connect = Button(
            self.root,
            text='ADB连接测试',
            command=self.connect_adb,
            font=15,
            bg='#87CEFF')
        connect.place(x=10, y=60)
        # 连接测试输入ip
        adb_ip = Entry(self.root, textvariable=self.v3)
        adb_ip.place(x=140, y=60, height=30)
        # 复选框CPU变量
        self.cpu_str = StringVar()
        self.cpu_str.set(0)
        # 复选框内存变量
        self.mem_str = StringVar()
        self.mem_str.set(0)
        # 复选框流量变量
        self.gprs_str = StringVar()
        self.gprs_str.set(0)
        # 复选框FPS变量
        self.fps_str = StringVar()
        self.fps_str.set(0)
        # 复选框温度变量
        self.tmp_str = StringVar()
        self.tmp_str.set(0)
        # 复选框总内存
        self.ram_str = StringVar()
        self.ram_str.set(0)
        # 复选框android版本变量
        self.android_str = StringVar()
        self.android_str.set(0)

        self.rom_str = StringVar()
        self.rom_str.set(0)
        # 复选框编译时间变量
        self.compile_date = StringVar()
        self.compile_date.set(0)
        # 复选框软件版本变量
        self.soft_version = StringVar()
        self.soft_version.set(0)
        # 监控对象
        check1 = Checkbutton(self.root, text='CPU',variable=self.cpu_str,
            offvalue=0,
            onvalue=1)
        check1.place(x=10, y=120)
        check2 = Checkbutton(self.root, text='内存',variable=self.mem_str,
            offvalue=0,
            onvalue=1)
        check2.place(x=80, y=120)
        check3 = Checkbutton(self.root, text='流量',variable=self.gprs_str,
            offvalue=0,
            onvalue=1)
        check3.place(x=150, y=120)
        check4 = Checkbutton(self.root, text='FPS',variable=self.fps_str,
            offvalue=0,
            onvalue=1)
        check4.place(x=220, y=120)
        check5 = Checkbutton(self.root, text='温度',variable=self.tmp_str,
            offvalue=0,
            onvalue=1)
        check5.place(x=290, y=120)
    #     监控按钮
        all_font = font.Font(family='宋体', size=20, weight=font.BOLD)
        start_button = Button(self.root, text='开始监控', bg="blue", font=all_font,command=self.new_window)
        start_button.place(x=10, y=170)


        # RAM
        check7 = Checkbutton(
            self.root,
            text='RAM',
            variable=self.ram_str,
            offvalue=0,
            onvalue=1)
        check7.place(x=10, y=230)
        # 安卓版本
        check7 = Checkbutton(
            self.root,
            text='安卓版本',
            variable=self.android_str,
            offvalue=0,
            onvalue=1)
        check7.place(x=90, y=230)
        # ROM
        check6 = Checkbutton(
            self.root,
            text='ROM',
            variable=self.rom_str,
            offvalue=0,
            onvalue=1)
        # check6.place(x=190, y=230)
        # 编译时间
        check_date = Checkbutton(
            self.root,
            text='编译时间',
            variable=self.compile_date,
            offvalue=0,
            onvalue=1)
        check_date.place(x=290, y=230)
        # 软件版本
        check_date = Checkbutton(
            self.root,
            text='软件版本',
            variable=self.soft_version,
            offvalue=0,
            onvalue=1)
        check_date.place(x=190, y=230)
        # android参数获取
        get_data = Button(
            self.root,
            text='版本信息',
            bg="orange",
            font=all_font,
            command=self.get_version)
        get_data.place(x=10, y=270)

        # 日志
        check10 = Checkbutton(self.root, text='日志')
        check10.place(x=10, y=330)
        # 报文
        check11 = Checkbutton(self.root, text='报文')
        check11.place(x=80, y=330)
        # 抓取
        data_button = Button(
            self.root,
            text='开始抓取',
            bg="DeepSkyBlue",
            font=all_font)
        data_button.place(x=10, y=380)

        # 日志清空
        button_clear = Button(
            self.root,
            text='清空日志',
            font=all_font,
            command=self.clerar_log,
            bg='red')
        button_clear.pack(side=RIGHT, expand=YES, fill=NONE, anchor=SE)

    def check_network(self):
        result = os.popen('adb devices').read()
        # print(result)
        hope_str = 'List of devices attached'
        if hope_str in result:
            self.log_data.insert('end', f"  ADB 环境正常\n\n{result}")
        else:
            self.log_data.insert(
                'end', "ADB环境   不   正常\n解决方案：\n1：检查是否成功下载 ADB 工具。\n2：是否配置 ADB 工具环境变量。\n\n")

    def connect_adb(self):
        threading.Thread(target=self.connect_adb1, args=()).start()
        threading.Thread(target=self.connect_adb2, args=()).start()

    def connect_adb1(self):
        self.log_data.insert('end', f" 正在测试，请等待大约15秒。。。。。\n\n")

    def connect_adb2(self):
        result = os.popen(f'adb connect {self.v3.get()}').read()
        # print(result)
        if 'unable' in result:
            self.log_data.insert('end', f"{result}\n")
            self.log_data.insert(
                'end', f"解决方案：\n1：检查机顶盒与计算机是否在同一个网段。\n2：检查机顶盒是否已经打开ADB功能。\n3：检查端口是否正确。\n\n")
        else:
            self.log_data.insert('end', f"{result}\n")

    def clerar_log(self):
        self.log_data.delete('1.0', 'end')

    def get_package(self):
        try:
            result = os.popen(
                f'adb shell dumpsys activity top | findstr ACTIVITY').read()
            self.log_data.insert('end', result)
            a = result.strip().split(' ')
            print(result)
            package_name = a[1].split('/')
            self.log_data.insert('end', f'  包名:  {package_name[0]}\n')
            self.log_data.insert('end', f'  类名:  {package_name[1]}\n\n')
            print(result)
        except BaseException:
            self.log_data.insert('end', '\n\t请检查设备是否在线\n\n')
            self.log_data.insert('end', os.popen('adb devices').read())

    def restart_adb(self):
        os.popen('adb kill-server')
        result = os.popen('adb start-server').read()
        if 'successfully' in result:
            self.log_data.insert('end', '  ADB重启成功\n\n')

    def get_version(self):
        if self.ram_str.get() == '1':
            # print(self.ram_str.get())
            threading.Thread(target=self.get_meninfo, args=()).start()
        if self.android_str.get() == '1':
            threading.Thread(target=self.get_android_version, args=()).start()
            # threading.Thread(target=,)
        # print(self.android_str.get())
        # print(self.rom_str.get())
        if self.compile_date.get() == '1':
            threading.Thread(target=self.get_date, args=()).start()
        # print(self.compile_date.get())
        if self.soft_version.get() == '1':
            threading.Thread(target=self.get_soft, args=()).start()
    # 获取运行内存

    def get_meninfo(self):
        cmd = ('adb shell dumpsys meminfo')
        # cmd以列表返回结果
        cpu_result = os.popen(cmd).read()
        result = re.findall(r'Total RAM: \d+ kB', cpu_result)[0]
        print(result)
        self.log_data.insert('end', f'{result}\n\n')
        # 获取版本信息

    def get_android_version(self):
        result = os.popen('adb shell getprop ro.build.version.release').read()
        # print(result)
        self.log_data.insert('end', f'\t安卓版本：{result}')

        # 获取编译时间
    # 获取
    def get_date(self):
        result = os.popen('adb shell cat /proc/version').read()
        a1 = result.strip().split(') #1')[1]
        # print(result)
        self.log_data.insert('end', f'{a1} \n\n')


    # 获取软件版本号
    def get_soft(self):
        result = os.popen('adb shell getprop|findstr incre').read()
        result = result.strip().split(':')[1]
        self.log_data.insert('end', f'软件版本号{result}\n\n')

    #     监控界面组件
    def new_window(self):
        # print(self.mem_str.get())
        # print(type(self.gprs_str.get()))
        self.new_master = Toplevel()
        self.new_master.title('监控中')
        self.new_master.geometry('590x450+150+100')
        # column表示列     columnspan 表示夸几列
        # row表示行        rowspan表示夸几行        sticky表示行内位置
        # minsize行高     pad 宽   padx水平方向外边距     pady垂直方向上的外边距
        # ipadx水平方向上的内边距    ipady垂直方向上的内边距
        Button(self.new_master, text='开始', command=self.start).grid(row=0, column=0, sticky='ewsn', padx=10)
        Button(self.new_master, text='暂停', command=self.change_state).grid(row=0, column=1, sticky='ewsn', padx=30)
        Label(self.new_master, text='时间').grid(row=1, column=0, sticky='ewsn', padx=20)
        Label(self.new_master, text='fps').grid(row=1, column=1, sticky='ewsn', padx=20)
        Label(self.new_master, text='cpu').grid(row=1, column=2, sticky='ewsn', padx=20)
        Label(self.new_master, text='内存').grid(row=1, column=3, sticky='ewsn', padx=20)
        Label(self.new_master, text='流量').grid(row=1, column=4, sticky='ewsn', padx=50)
        Label(self.new_master, text='温度').grid(row=1, column=5, sticky='ewsn', padx=50)

        sb = Scrollbar(self.new_master, orient='vertical', width=25)
        sb.grid(row=2, column=6, sticky='ns')
        self.lb = Listbox(self.new_master, yscrollcommand=sb.set, height=20)
        # for i in range(100):
        #     lb.insert(i, f'2019-1-1   25      67    {i} ')
        self.lb.grid(row=2, column=0, columnspan=6, sticky='we')
        sb.config(command=self.lb.yview)
        # self.get_time()
    # 开始按钮的回弹作用
    def start(self):
        threading.Thread(target=self.mainfunc, args=()).start()
    # 暂停按钮控制
    def change_state(self):
        # 点击暂停，更改属性标识
        self.state=False
    # 开始监控主控制
    def mainfunc(self):
        # print(type(self.gprs_str.get()))
        self.state=True
        while True:
            # 判断状态标识为True，则为持续更新状态，否则退出循环
            if self.state==True:
                self.get_information()
                date = time.strftime('%H:%M:%S', time.localtime(time.time()))
                if self.cpu_str.get()=='1':
                    cpu = self.get_cpu()
                else:
                    cpu='无'
                if self.fps_str.get()=='1':
                    fps=self.get_fps()
                else:
                    fps='无'
                if self.tmp_str.get()=='1':
                    tmp=self.get_temperature()
                else:
                    tmp='无'
                if self.mem_str.get()=='1':
                    mem=str(self.get_meninfo1())+'%'
                else:
                    mem='  无'
                if self.gprs_str.get()=='1':
                    a=self.get_gprs()
                    gprs0='下载'+a[0]+'M'
                    gprs1='上传'+a[1]+'M'
                    gprs=gprs0+','+gprs1
                else:
                    gprs='         None            '
                # 内存 、流量 温度
                try:
                    # if gprs=='无' and mem=='无' and tmp=='无' and
                    self.lb.insert(0, f'{date}              {fps}                  {cpu}            {mem}           {gprs}              {tmp}')
                except:
                    break
            else:
                break
#    获取cpu
    def get_cpu(self):
        result = os.popen('adb shell dumpsys cpuinfo').read()
        a = re.findall('(\d{,3}|\d\.\d)% TOTAL', result)
        # print(result)
        # print(a)
        w = a[0]
        return w

    # 获取当前运行的apk包名、类名、pid
    def get_information(self):
        cmd = 'adb shell dumpsys window | findstr mCurrentFocus'
        result = os.popen(cmd).read().strip().split()[-1].split('}')[0].split('/')
        self.packagename = result[0]
        self.activityname = result[1]
        cmd = f'adb shell ps |findstr {self.packagename}'
        result = os.popen(cmd).read()
        self.pid = re.findall(' \d+ ', result)[0]
        result2 = os.popen(f'adb shell dumpsys package {self.packagename} | findstr userId').read()
        self.userId = result2.strip().split()[0].split('=')[1]
        # print(self.packagename, self.activityname, self.pid, self.userId)

    # 获取FPS
    def get_fps(self):

        pkg_name=self.packagename
        _adb = "adb shell dumpsys gfxinfo %s" % pkg_name
        # print(_adb)
        results = os.popen(_adb).read().strip()
        # print(results)
        frames = [x for x in results.split('\n') if validator(x)]
        # print(frames)
        frame_count = len(frames)
        jank_count = 0
        vsync_overtime = 0
        render_time = 0
        for frame in frames:
            time_block = re.split(r'\s+', frame.strip())
            if len(time_block) == 3:
                try:
                    render_time = float(time_block[0]) + float(time_block[1]) + float(time_block[2])
                except Exception as e:
                    render_time = 0

            '''
            当渲染时间大于16.67，按照垂直同步机制，该帧就已经渲染超时
            那么，如果它正好是16.67的整数倍，比如66.68，则它花费了4个垂直同步脉冲，减去本身需要一个，则超时3个
            如果它不是16.67的整数倍，比如67，那么它花费的垂直同步脉冲应向上取整，即5个，减去本身需要一个，即超时4个，可直接算向下取整

            最后的计算方法思路：
            执行一次命令，总共收集到了m帧（理想情况下m=128），但是这m帧里面有些帧渲染超过了16.67毫秒，算一次jank，一旦jank，
            需要用掉额外的垂直同步脉冲。其他的就算没有超过16.67，也按一个脉冲时间来算（理想情况下，一个脉冲就可以渲染完一帧）

            所以FPS的算法可以变为：
            m / （m + 额外的垂直同步脉冲） * 60
            '''
            if render_time > 16.67:
                jank_count += 1
                if render_time % 16.67 == 0:
                    vsync_overtime += int(render_time / 16.67) - 1
                else:
                    vsync_overtime += int(render_time / 16.67)

        _fps = int(frame_count * 60 / (frame_count + vsync_overtime))

        # return (frame_count, jank_count, fps)
        # print("-----fps------")
        # print(_fps)
        return _fps
        # 获取温度
    # 获取温度
    def get_temperature(self):
        cmd = 'adb shell cat /sys/devices/virtual/thermal/thermal_zone0/temp'
        result = os.popen(cmd).read()
        return result

    # 获取内存使用百分比
    def get_meninfo1(self):
        # cmd输入内容
        # connect(ip)
        cmd = ("adb  shell  dumpsys  meminfo ")
        # print(cmd)
        # cmd以列表返回结果
        mem_result = os.popen(cmd).read()
        # print(mem_result)
        ram = re.findall('Total RAM: \d+ kB', mem_result)[0].strip().split(' ')[2]
        # print(ram)
        use_mem = re.findall('Used RAM: \d+ kB', mem_result)[0].strip().split(' ')[2]
        # print(use_mem)
        result_use=int(int(use_mem)/int(ram)*100)
        # print(result_use)
        return result_use
    # 获取流量
    def get_gprs(self):
        pid = self.pid
        pid = int(pid)
        cmd = f'adb shell cat /proc/{pid}/net/dev'
        # cmd=f'adb shell cat /proc/6124/net/dev'
        result = os.popen(cmd).readlines()
        # print(result)
        for i in result:
            if 'eth0:' in i:
                # print(i)
                gprs = re.findall('\d{4,}', i)
                # print(gprs)
                Receive_gprs = round(float((int(gprs[0]) / 1024 / 1024)), 2)
                Receive_gprs='%.2f'%Receive_gprs
                Transmit_gprs = round(float((int(gprs[2]) / 1024 / 1024)), 2)
                Transmit_gprs='%.2f'%Transmit_gprs
                # print("下载流量：" + Receive_gprs + ' M', "上传流量：" + Transmit_gprs + ' M')
                return str(Receive_gprs),str(Transmit_gprs)


if __name__ == '__main__':
    # A=Login(master=Tk())
    # if A.user_stste==True:
        Test_interface(master=Tk())
