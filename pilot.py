import traceback
import time
import re
import sys
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


mailTime = time.strftime('%Y-%m-%d %H:%M:%S')


## find key words timeout in otdf loader logs, if found more than 0, send out emails
filepath="D:\\OTLogs\\monitorOTDFloaderLogs.log"

try:
    
    fp=open(filepath,"r")
    logger.debug('start openning otdf loader log file' )
except IOError as e:
    print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    logger.debug('can not open otdf loader log file' , filepath )
    logger.exception("message")
else:
    print("log file reading completed")
    logger.debug('OTDF Loader logs reading completed ')
    icount=1
for s in fp.readlines():  
    li=re.findall("timeout", s)  
    if len(li)>0:
        icount=icount+len(li)
    fp.close()

    
print("find:",icount,">>> timeout in OTDF Loading failed log")

if icount>1:
    print("find:",icount,">>> timeout in logs , going to send alert emails")
    logger.debug('found timeout in logs , going to send alert emails')
    logger.debug('an email has been sent at ' + mailTime)
    print ("mail sent")

if icount==1:
    print("find:",icount,">>> timeout, NOT going to send alert emails")
logger.debug('no timeout found in logs , NOT going to send alert emails')


exit(0)

    
