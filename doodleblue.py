import datetime
import io
import json
import sys
import calendar

class Doodle:

    def __init__(self):#constructor class
        self.schedule=1#initialize schedule
        self.id1=1#initialize id

    def getjson(self):#get string and converts into json_array
        self.string=input("Enter the data in json format: ")#gets string
        self.json_array=json.loads(self.string)#converts into json array using load function

    def check_days(self):#check days
        self.weekdays=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
        self.input=[]
        for i in self.json_array:#check whether the days are valid days if "fridis" is given it returns False else True
            i=i.strip()   #it removes spaces in front and back of the string
            
            if i.lower() in self.weekdays:
                if i.lower() in self.input:# if ["monday","wednesday","wednesday"] is given It changes to ["monday","wednesday"]
                    pass
                else:
                    self.input.append(i.lower())
                count=True
            else :
                count=False
                break#loops breaks when there is invalid data
        return count
    
    

    def writefile(self):#writing output to the csv file which shows the output in the table format
        now=datetime.date.today()#it gets the current date
        filename="schedule.csv"# csv file name it will be created in the working directory
        f=io.open(filename,"w",encoding="utf-8")#opening a csv five in write mode
        headers="ID, Day, Schedule, Current_datetime \n"
        f.write(headers)#writing the column headers into csv file
        for i in range(1,29):
            day=calendar.day_name[now.weekday()]#it returns weekdays [ie:Monday,Tuesday,Wednesday,etc] of the date 
            if day.lower() in self.input:#it checks whether the current day has to be schedule or not
                current_datetime=(str(now).replace("-",".")+"."+str(datetime.datetime.now().time()))#it concatenates date and time
                
                f.write(str(self.id1)+"\t" + "," + str(day.upper())+"\t"  + "," + str(self.schedule)+"\t"  + "," + current_datetime +"\n")#it writes id , weekday,schedule,datetime
                self.id1+=1
                self.schedule+=1
            now= datetime.date.today()+datetime.timedelta(days=i)#it increments next day
        f.close()# file closed

doodle=Doodle()#creating object for class
doodle.getjson()
n=doodle.check_days()
if n==True:#if valid days is given it writes into the file else quit
    doodle.writefile()
    print("Your days Scheduled successfully")
    print("Open your working directory and open Schedule.csv file")
    print("Note :Click Yes and OK while opening csv file ")#caution
else:
    print("Inalid days")
    quit()



