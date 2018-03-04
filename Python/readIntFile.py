#!/usr/bin/python

import sys
import time

def main():
  myFilName = sys.argv[2]
  nbrOfSorts = int(sys.argv[1])
  outFileName = sys.argv[3]

  myFile = open(myFilName)
  myList = []
  myTimes = []
  for line in myFile.readlines():
    myList.append(int(line))
  myFile.close()

  """ new_listu = list(myList)
  new_listu.sort()
  outFileu = open('testSortedInt.txt','w')
  for x in range(0, len(new_listu)):
   if x==len(new_listu)-1:
       outFileu.write("%s" % new_listu[x])
   else:
     outFileu.write("%s\n" % new_listu[x])
  outFileu.close()"""



  for x in range(0, nbrOfSorts):
    new_list = list(myList)
    timeStart = time.clock()
    new_list.sort()
    timeStop = time.clock()
    totTime = (timeStop-timeStart)*10**6
    myTimes.append("%.2f" % totTime)
    new_list = None

  outFile = open(outFileName,'w')
  for x in range(0, len(myTimes)):
      s1 = "%s" % (x+1)
      s2 = "%s" % myTimes[x]
      s3 = "%s\n" % myTimes[x]
      if x==len(myTimes)-1:
          outFile.write(s1+', '+s2)
      else:
        outFile.write(s1+', '+s3)
main()
