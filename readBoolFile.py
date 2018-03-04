#!/usr/bin/python

import sys
import time

def main():
  myFilName = sys.argv[2]
  nbrOfSorts = int(sys.argv[1])
  outFileName = sys.argv[3]


  myList = []
  myBolList = []
  myTimes = []

  with open(myFilName) as myFile:
    myList = [line.rstrip('\n').rstrip('\r') for line in myFile]
  myFile.close()


  for x in myList:
     if x == "true":
         myBolList.append(True)
     elif x == "false":
         myBolList.append(False)

  """ new_listu = list(myBolList)
  new_listu.sort()
  outFileu = open('testSortedBol.txt','w')
  for x in range(0, len(new_listu)):
    if x==len(new_listu)-1:
        outFileu.write("%s" % new_listu[x])
    else:
      outFileu.write("%s\n" % new_listu[x])
  outFileu.close()"""

  for x in range(0, nbrOfSorts):
    new_list = list(myBolList)
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
