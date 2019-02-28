import datetime
import time
from tkinter import Label


def helloworld():
        s='hello world'
        print(s)
if __name__=='__main__':
 helloworld()
 iday = datetime.date.today() - datetime.timedelta(days=35)
 print(iday)
 #listthings=['a','b','c','d']
 #widget=Label(None, text='Hello GUI Python ! '+ listthings[1])
 #widget.pack()
 #widget.mainloop()
 t1="1982-11-24 04:49:13"
 t1t=datetime.datetime.strptime(t1, "%Y-%m-%d %H:%M:%S")
 t2='2017-08-10 11:51:13'
 t2t=datetime.datetime.strptime(t2, "%Y-%m-%d %H:%M:%S")
 timestamp1=time.mktime(t1t.timetuple())
 timestamp2=time.mktime(t2t.timetuple())

 gaptime=(timestamp2-timestamp1)/60/60/24/365

 print(gaptime)