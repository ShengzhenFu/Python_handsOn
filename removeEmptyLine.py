import sys
def removeEmptyLine(infile, outfile):
    infopen=open(infile,'r')
    outfopen=open(outfile,'w')
    lines=infopen.readlines()
    
    for line in lines:
        if line.split():
            outfopen.writelines(line)
        else:
            outfopen.writelines("")
    infopen.close()
    outfopen.close()
    
if __name__=='__main__':
    removeEmptyLine("D:\\OTLogs\\Testers_haveEmptylines.csv","D:\\OTLogs\\123.csv")
