# -*- coding: utf-8 -*-
import traceback
from email.header import Header
import smtplib
from email.mime.multipart import MIMEMultipart


def send_email(to_addr_in, cc_addr_in):
    from_addr = 'xxxx@163.com'
    smtp_server = 'smtp.163.com'
    password = 'xxxxx'
    to_addr = to_addr_in
    to_addrs = to_addr.split(',')
    cc_addr = cc_addr_in
    cc_addrs = cc_addr.split(',')
    msg = MIMEMultipart()
    msg['From'] = from_addr
    # msg['To'] = to_addr    # single receiver
    msg['To'] = ",".join(to_addrs)  # multi receiver
    msg['Subject'] = Header('mail from python sendmail', 'utf-8').encode()  # subject

    try:
        server = smtplib.SMTP(smtp_server, 25)
        # server.starttls()
        server.set_debuglevel(1)  # 用于显示邮件发送的执行步骤
        server.login(from_addr, password)
        # print to_addrs
        server.sendmail(from_addr, to_addrs+cc_addrs, msg.as_string())
        server.quit()
    except Exception as e:
        print("Error: unable to send email")
        print(traceback.format_exc())


if __name__ == '__main__':
    send_email('xxxx@qq.com,xxxx@163.com', 'xxxx@qq.com,xxxx@163.com')
