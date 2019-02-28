##  revision history                                                          ###
##                                                                            ###
import time
import smtplib  
from email.mime.text import MIMEText

mail_from='FSLCHSCOMNotification@optimalplus.com'
mail_to='Shengzhen.Fu@optimalplus.com'
mail_host='10.64.34.197'
mail_user=''
mail_pass=''
mail_port='25'
mail_time= time.strftime('%Y-%m-%d %H:%M:%S')
mail_sub='[Notice]email of OTDF loader timeout at ATTJ'
mail_body='hi OT support found timeout in OTDF loader logs today at ATTJ , please check and reload if required, thanks'

def SendMail():
    msg= MIMEText(mail_body)
    msg['Subject']= mail_sub
    msg['From']= mail_user
    msg['To']= mail_to
    
    try:
        server= smtplib.SMTP(mail_host, mail_port)
        server.connect(mail_host)
        server.set_debuglevel(1)
        server.ehlo()
        #server.starttls()
        #server.login(mail_user, mail_pass)
        server.sendmail(mail_from, mail_to, msg.as_string())
        server.close()
        print("successfully sending mail")
    except Exception as e:
        print(str(e))
if __name__=='__main__':
    SendMail()
