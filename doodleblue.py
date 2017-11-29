import datetime
import io
import json
import sys
class Doodle:

    def __init__(self):
        self.schedule=1
        self.id1=1

    def getjson(self):
        self.string=input("Enter the data in json format: ")#gets string
        self.json_array=json.loads(self.string)#converts into json array using load function

    def check_days(self):
        for i in self.json_array:
            i=i.strip()
            if i.lower()=="monday" or i.lower()=="tuesday" or i.lower()=="wednesday" or i.lower()=="thursday" or i.lower()=="friday" or i.lower()=="saturday" or i.lower()=="sunday":
                count=True
            else:
                count=False
                break
        return count
    def date(self):
        self.now=datetime.datetime.now()
        self.current_datetime=self.now.strftime("%Y-%m-%d %H:%M")

    def writefile(self):
        
        filename="schedule.csv"
        f=io.open(filename,"w",encoding="utf-8")
        headers="ID , Day , Schedule , Current_datetime \n"
        f.write(headers)

        for i in range(28):
            day=self.json_array[self.schedule%len(self.json_array)].strip()
            f.write(str(self.id1) + "," + str(day.upper()) + "," + str(self.schedule) + "," + self.current_datetime.replace(" ",".") +"\n")
            self.id1+=1
            self.schedule+=1

        f.close()

doodle=Doodle()
doodle.getjson()
n=doodle.check_days()
if n==True:
    doodle.date()
    doodle.writefile()
    print("Your days Scheduled successfully")
    print("Open your working directory and open Schedule.csv file")
    print("Note :Click Yes ")
else:
    print("Inalid days")
    quit()



