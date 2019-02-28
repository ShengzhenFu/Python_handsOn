import re
import os
import sys
import linecache
import shutil

outputFile="D:\\OTLogs\\LoadingFailedFileList.log"
if os.path.exists(outputFile):
    print("great, the file already exists")
else:
    print("going to create output file")
    fo=open(outputFile,'w')
    print("file created")
logfile="D:\\OTLogs\\OtdfDataLoader.log"

w1="System.AggregateException: One or more errors occurred. ---> System.Data.SqlClient.SqlException: Execution Timeout Expired"
w2="Loading failed for file "
f=open(logfile,'r')
s=f.readlines()
f.flush()
f.close()
def findfailedOTDFtoLogs():
    for i in range(0,len(s)-1):       
       if s[i].startswith(w1):          
            result=re.findall('.*'+w2+'(.*):.*', s[i-1])
            print(result)     
            with open(outputFile,'a') as file_handler:                
                 file_handler.write(str(result).replace(']','\n').replace('[','').replace('\'',''))                                
                 file_handler.close()           
if __name__=='__main__':
    findfailedOTDFtoLogs()
    m=open(outputFile, 'r')
    n=len(m.readlines())
    m.close()
    print(n)
    
    for j in range(1, n+1):
        otdf_file_name=linecache.getline(outputFile, j)        
        shutil.move("D:\\OTLogs\\"+otdf_file_name.strip(), "F:\\g\\"+otdf_file_name.strip())
        j+=j 
