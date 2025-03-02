import re
import requests
import ssl
import time
import random
import os
import subprocess

log_file_path = 'log.txt'

# post_URL = 'https://sam.zwu.edu.cn/eportal/InterFace.do?method=login' 这是一个示例，请阅读README
post_URL = ''

header = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Connection": "keep-alive",
            "Content-Length": "661",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "",
            "Host": "sam.zwu.edu.cn",
            "Origin": "https://sam.zwu.edu.cn",
            "Referer": "",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
        }
# 示例头文件，请根据README修改
# 检测网络是否已登录
def ping_test():
    try:
        # 执行ping命令
        response = subprocess.run(['ping', 'www.baidu.com', '-n', '1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # 请注意，如果是windows环境下运行请使用-n参数，如果在linux下运行请使用-c参数
        if response.returncode == 0:  # 如果ping成功，返回0
            print("网络已连接，已登录。")
            return True
        else:
            print("未连接网络，未登录。")
            return False
    except Exception as e:
        print(f"Ping 测试失败: {e}")
        return False


# 登录过程
def login():
    print("正在执行登录操作...")

    # 设置post的请求数据
    data = {
        "userId": '',  # 校园网账号，请根据README填写
        "password": '',  # 校园网密码（密文），请根据README填写
        "queryString": '', #请根据README填写
        "passwordEncrypt": 'true',
        "operatorPwd": '',
        "operatorUserId": '',
        "validcode": '',
        "service": 'default', #请根据README填写
    }

    # 发送POST请求
    response = requests.post(post_URL, data, headers=header)

    print("登录 POST 请求状态码:", response.status_code)

    # 解析响应为JSON格式
    response_json = response.json()  # 解析JSON响应

    # 打印响应内容
    print("登录响应内容:", response_json)

    # 检查result是否为success
    if response_json.get("result") == "success":
        print("登录成功！")
        return True
    else:
        print("登录失败！")
        return False
# 如需仅使用脚本实现定时测试并自动连接请使用循环
def run_script():
    print("脚本开始执行")
    if ping_test():
        print("无需执行登录逻辑。")
    else:
        print("开始执行登录操作...")
        login()

    # 将每次日志内容写入log文件
    with open(log_file_path, 'a', encoding='utf-8') as log_file:
        log_file.write("自动联网脚本开始运行...\n")
        log_file.write(f"当前时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        log_file.write(f"网络连接状态: {'已登录' if ping_test() else '未登录'}\n")
    

# 执行主程序
if __name__ == "__main__":
    run_script()
