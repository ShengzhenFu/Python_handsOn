## this program is to monitor OTDF loader logs which have timeout issue       ###
## it will send email alert to OT support to check and reload the OTDF files  ###
## 9am 15/Sep 2017 created by Shengzhen.Fu@optimalplus.com                    ###
##  revision history                                                          ###
##                                                                            ###
 
import time
import re
import sys
import smtplib  
from email.mime.text import MIMEText   

import logging  
import logging.handlers  
##beginning of send email function
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
        server.sendmail(mail_from, mail_to, msg.as_string())
        server.close()
        print("successfully sending mail")
    except Exception as e:
        print(str(e))
##end of send email function

LOG_FILE = 'D:\\OTLogs\\monitorOTDFloaderLogs.log'  
  
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5)   
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'  
  
formatter = logging.Formatter(fmt)   # instance the formatter  
handler.setFormatter(formatter)      # add formatter  to handler
  
logger = logging.getLogger(LOG_FILE)    # obtain tst logger  
logger.addHandler(handler)           # add handler in logger
logger.setLevel(logging.DEBUG)  

## find key words timeout in otdf loader logs, if found more than 0, send out emails
filepath="D:\\OTLogs\\OtdfDataLoader.log"

try:
    fp=open(filepath,"r")
    logger.debug('start openning otdf loader log file' )
except IOError as e:
    print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    logger.debug('can not open otdf loader log file' , filepath )
    logger.exception("message")
count=0;  
for i in fp.readlines():  
    li=re.findall("timeout", i)  
    if len(li)>0:              
        count=count+len(li)      
print("find:",count,">>> timeout in OTDF Loading failed log")
logger.debug('OTDF Loader logs reading completed ')
fp.close()

if count > 0:
    logger.debug('found timeout in logs , going to send alert emails')
    SendMail()

if count==0:
    logger.debug('no timeout found in logs , NOT going to send alert emails')
sys.exit()

    
