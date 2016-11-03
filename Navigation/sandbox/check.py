import Navigation.prod.Angle as Angle
from datetime import datetime
from datetime import timedelta
import csv
anAngle = Angle.Angle()
starData = []
with open('stars.txt','r') as f:
    data = csv.reader(f,delimiter='\t')
    for row in data:
        body = row[0]
        newdate = row[1]
#        newdate = datetime.strptime(row[1],"%m/%d/%y")
        longitudedegreeMinute = anAngle.setDegreesAndMinutes(row[2])
        latitudedegreeMinute = row[3]
        starData.append([body,newdate,longitudedegreeMinute,latitudedegreeMinute])
f.close()
starData.sort()
for row in starData:
    print(row)
    dt = datetime.strptime(str(row[1]), "%m/%d/%y").date() + timedelta(days=1)
    print(datetime.strftime(datetime.strptime(row[1], "%m/%d/%y").date(),"%Y-%m-%d"))

    print(row[1],datetime.strftime(dt,"%m/%d/%y"))
#    print(row[1],datetime(row[1])+ timedelta(days=1) )