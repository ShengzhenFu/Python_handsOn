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
from email.header import Header  

import logging  
import logging.handlers  
  
LOG_FILE = 'D:\\OTLogs\\monitorOTDFloaderLogs.log'  
  
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5)   
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'  
  
formatter = logging.Formatter(fmt)   # instance the formatter  
handler.setFormatter(formatter)      # add formatter  to handler
  
logger = logging.getLogger(LOG_FILE)    # obtain tst logger  
logger.addHandler(handler)           # add handler in logger
logger.setLevel(logging.DEBUG)  

logger.debug('prepare smtp settings')


## definition for smtp and email variables
default_encoding = 'utf-8'  
if sys.getdefaultencoding() != default_encoding:  
    reload(sys)  
    sys.setdefaultencoding(default_encoding)  
encoding = 'utf-8'

smtpHost = '10.64.34.197'
smtpPort = '25'
#sslPort = '587'
fromMail = 'FSLCHSCOMNotification@optimalplus.com'
toMail = 'Shengzhen.Fu@optimalplus.com'
username = ''  
password = ''  
mailTime = time.strftime('%Y-%m-%d %H:%M:%S')

subject = u'[Notice]email of OTDF loader timeout at ATTJ ' + (mailTime)
body = u'hi OT support found timeout in OTDF loader logs today at ATTJ '+ (mailTime) + 'please check and reload if required, thanks' 

encoding = 'utf-8'
mail = MIMEText(body.encode(encoding),'plain',encoding)  
mail['Subject'] = Header(subject,encoding)  
mail['From'] = fromMail  
mail['To'] = toMail  


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

if count > 0:logger.debug('found timeout in logs , going to send alert emails')
try:
    server = smtplib.SMTP(smtpHost,smtpPort)
    server.connect(smtpHost)
    server.set_debuglevel(1)
    server.ehlo()
    #server.starttls()
    #server.login(username,password)

    server.sendmail(fromMail,toMail,mail.as_string())  
    server.close()
    logger.debug('an email has been sent at ' + mailTime)
    print ("mail sent")

except Exception as e:  
    print (str(e))
logger.exception("message")

if count==0:logger.debug('no timeout found in logs , NOT going to send alert emails')
exit(0)

    
