import subprocess
import os
import re
# 连接adb
import time


def connect(ip):
    connect_result=subprocess.Popen(f"adb connect {ip}")
    print(connect_result)

# 获取内存使用情况
def get_meninfo(ip):
    # cmd输入内容
    # connect(ip)
    cmd=("adb -s %s shell  dumpsys  meminfo " % (ip))
    # print(cmd)
    # cmd以列表返回结果
    cpu_result=os.popen(cmd).readlines()
    # cpu_result=str(subprocess.check_output(cmd))
    print(cpu_result)
    for i in cpu_result:
        if 'Total RAM' in i:
            total_cpu=re.findall("(.*?)K",i)[0]
            # li=i.strip('')
            print(total_cpu)
        if 'Free RAM' in i:
            free_cpu = re.findall("(.*?)K", i)[0]
            # li=i.strip('')
            print(free_cpu)
        if 'Used RAM' in i:
            use_cpu=re.findall("(.*?)K",i)[0]
            # li=i.strip('')
            print(use_cpu)
# 获取cpu使用情况
def get_cpuinfo(ip):
    # find_number为查看cpu占用排名前面的数量
    find_number=5
    cmd=f'adb shell top -n 1 -m {find_number}'
    cpuresult=os.popen(cmd).readlines()[-2*find_number:-1]
    li=[]
    dic={}
    for i in cpuresult:
        if i !='\n':
            li.append(i)
    # print(li)
    for i in li:
        # time.sleep(0.5)
        number=re.search(r'(((S|R|D) {1,2})(((\d){1,2}\.\d)|((\d){3})))',i).group().split(' ')[-1]
        name=re.search(r':\d{2}\.\d{2} (.*?)\n',i).group().strip().split(' ',1)[1]
        # print(name)
        dic[name]=number
    time.sleep(0.5)
    print(dic)
# 获取当前运行的apk包名、类名、pid
def get_information():
    cmd = 'adb shell dumpsys window | findstr mCurrentFocus'
    result = os.popen(cmd).read().strip().split()[-1].split('}')[0].split('/')
    packagename = result[0]
    activityname = result[1]
    cmd = f'adb shell ps |findstr {packagename}'
    result = os.popen(cmd).read()
    pid = re.findall(' \d+ ', result)[0]
    result2 = os.popen(f'adb shell dumpsys package {packagename} | findstr userId').read()
    userId = result2.strip().split()[0].split('=')[1]
    print(packagename,activityname,pid,userId)
    return packagename,activityname,pid,userId
# 获取流量wifi
def get_gprs(pid):
    cmd=f'adb shell cat /proc/{pid}/net/dev'
    result=os.popen(cmd).readlines()
    # print(result)
    for i in result:
        if ' wlan0:'in i:
            # print(i)
            gprs=re.findall('\d{4,}',i)
            Receive_gprs=str(round(float((int(gprs[0])/1024/1024)),2))
            Transmit_gprs=str(round(float((int(gprs[2])/1024/1024)),2))
            print("下载流量："+Receive_gprs+' M',"上传流量："+Transmit_gprs+' M')
# 获取android温度
def get_temperature():
    cmd='adb shell cat /sys/devices/virtual/thermal/thermal_zone0/temp'
    result=os.popen(cmd).read()
    temperature_result= str(int(result)/1000)
    print("当前温度为："+temperature_result+" ℃")
if __name__ == '__main__':
    # get_meninfo("10.6.252.236:8278")
    while 1:
    #     # get_cpuinfo("192.168.0.101:5555")
    #     time.sleep(10)
    #     # get_meninfo("192.168.0.101:5555")
    #     pass
    #     get_information()
    #     li=['20302','20615','20689','20852','20999']
    #     for i in li:
            get_gprs(11525)
    #         print(i)
            time.sleep(3)
    # 下载347M 上传12M
    # [2876250345] [1659740155]