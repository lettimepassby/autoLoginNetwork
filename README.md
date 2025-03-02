![image](https://github.com/user-attachments/assets/59890344-dbbb-4253-87c8-4945fbdacf3e)# autoLoginNetwork
自动登录校园网脚本
该脚本实现逻辑：每次执行时尝试ping网站，如果不通表明校园网认证未通过，执行登录逻辑，可以ping通表明认证通过便不再进行登录操作
脚本需要配置四块地方：
1. post_URL
2. header
3. ping_test
4. data
### 配置post_URL
进入校园网登录认证界面，打开开发者工具（按下f12）进入网络界面（netword）并勾选保留日志
![image](https://github.com/user-attachments/assets/874c2d4b-36d6-4c8d-afe0-d153415764e3)
正常输入账号密码进行登录
![image](https://github.com/user-attachments/assets/3749ab7d-d70b-48b2-840b-d4689fc63438)
找到InterFace.do?method=login的数据包，点击打开
![image](https://github.com/user-attachments/assets/a70fc959-230d-4e5e-b296-f868556d6b16)
请求 URL即需要配置的post_URL
### 配置header
在相同界面向下滑动找寻到请求标头栏
![image](https://github.com/user-attachments/assets/bfdab32a-3def-4bed-bc64-f338c35d52d5)
请求标头栏即为所需header，请转化为对应格式
### 配置ping_test
该配件仅在使用linux运行脚本时需要修改
在windows环境下保持原样即可，linux环境下请使用-c参数而不是-n
### 配置data
依旧是在相同界面下，点击进入负载页面
![image](https://github.com/user-attachments/assets/ebb2c4f8-30cf-485e-b802-8eef7fae62b2)
负载即为data内参数，根据内容修改增加即可

## 常见问题
'''ssl.SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] ssl/tls alert handshake failure (_ssl.c:1006)'''
请降低urllib3版本后运行
'''pip install urllib3==1.26.5'''
