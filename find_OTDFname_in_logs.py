import re

logfile="D:\\OTLogs\\OtdfDataLoader3.log"
#def find_filename():        
#        w1="Loading failed for file "
#        w2="System.AggregateException: One or more errors occurred"
#        f=open(logfile,'r')
#        print("open log file now")        
#        buff=f.read()    
#        buff=buff.replace('\n','')
#        pat=re.compile(w1+'(.*?)'+w2,re.S)
#        result=pat.findall(buff)
#        print(result)
#        f.close()
        
#        w1="Loading failed for file "
#       w2="System.AggregateException: One or more errors occurred"
#      f=open(logfile,'r')
#     print("open log file now")
#    pat=re.compile(w1+'(.*?)'+w2,re.S)
#   print(pat)
#  for buff in f.readlines():                                      
#                result=pat.findall(buff)
#                print(result)
#        f.close()
w1="Loading failed for file "
w2="System.AggregateException: One or more errors occurred"
f=open(logfile,'r')        
s=f.readlines()
f.flush()
f.close()
for fileLine in s:
    if  w1 in fileLine:        
        line_pattern1 =r'\s*\d+\s?(.*)'
        print(fileLine)
for fileLine2 in s:
    if w2 in fileLine2:
        line_pattern2 =r'\s*\d+\s?(.*)'
        print(fileLine2)
        def func(text):
            c = re.compile(line_pattern1+'(.*?)'+line_pattern2, re.S)
            print(c)
            lists = []
            lines = text.split('\n\r')
            for line in lines:
                r = c.findall(line)
                if r:
                    lists.append(r[0])
            return '\n\r'.join(lists)
        
        result = func(fileLine)
        print(result)
        #test=[]
        #test.append(result)
        #print (test)

