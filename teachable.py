
import csv
import pandas
def addData(data1, data2):
  with open('knowledge.csv', 'a') as csvfile:
    mywriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    data1 = str(data1).lower()
    data2 = str(data2).lower()
    mywriter.writerow([data1, data2])
def checkInData(query):
  myQues = []
  with open('knowledge.csv', 'r') as f:
      reader = csv.reader(f)
      for row in reader:
          myQues.append(row[0])
  lenQues = len(myQues)
  i  = 1
  while(i < lenQues):
    if(myQues[i] == query):
      return 1
    i = i +1
  return 0
def addResponse(query):
  print("The Question was: ", query)
  data1 = input("Enter its response: ")
  addData(query.lower(), data1.lower())
  print("Thanks for teaching PyBot!")
def botRespond(query):
  myQues = []
  myResp = []
  with open('knowledge.csv', 'r') as f:
      reader = csv.reader(f)
      for row in reader:
          myQues.append(row[0])
  with open('knowledge.csv', 'r') as r:
      reader1 = csv.reader(r)
      for row1 in reader1:
          myResp.append(row1[1])
  lenQues = len(myQues)
  i  = 1
  while(i < lenQues):
    if(myQues[i] == query.lower()):
      print(myResp[i])
    i = i + 1
print("Hello!")
while(True):
  thisResponse = input("\t: ")
  if(thisResponse.lower() == "bye" or thisResponse.lower() == "goodbye"):
    break
  findVal = checkInData(thisResponse.lower())
  if(findVal == 1):
    botRespond(thisResponse)
  else:
    addResponse(thisResponse)
print("Thanks for chatting!")
