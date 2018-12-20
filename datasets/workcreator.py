# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
workfile=open('work.txt','r')
works=list(workfile)
workfile.close()
remarkfile=open('remark.txt','r')
remarks=list(remarkfile)
remarkfile.close()

inputfile=open('input.txt','w')
minutelist=['10','20','30','40','50','00']
hourlist=['5','6','7','8']
ampmlist=['AM','PM']


def main():
    for i in range(0,10000):
        inputfile.write("Work Done: "+works[random.randrange(0,works.__len__())])
        starthour=hourlist[random.randrange(0,hourlist.__len__())]
        endhour=int(starthour)+2
        startminutes=minutelist[random.randrange(0,minutelist.__len__())]
        workminutes=minutelist[random.randrange(0,minutelist.__len__())]
        endminutes=int(startminutes)+int(workminutes)
        if int(endminutes)>60:
            endminutes = int(endminutes) - 60
        if(endminutes==60):
            endminutes=00
        inputfile.write("Start Time: "+ starthour +":"+startminutes+'\n')
        inputfile.write("End Time: "+ str(endhour) +":"+str(endminutes)+'\n')
        if workminutes=='00' :
            inputfile.write("Duration: "+'2 hours '+'\n');
        else:
            inputfile.write("Duration: "+'2 hours '+ workminutes+ " minutes"+'\n')
        inputfile.write("Remarks: "+remarks[random.randrange(0,remarks.__len__())]+'\n')
    inputfile.close()

if __name__=='__main__':
    main()
