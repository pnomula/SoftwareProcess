from datetime import datetime
from datetime import timedelta
import xml.etree.ElementTree as ET
import Navigation.prod.Angle as Angle
import sys
import os.path as op
import time
import pytz
import math
import csv
class Fix:
    def __init__(self,logFile="log.txt"):
        functionName = "Fix.__init__:"
        self.angle = Angle.Angle()
        self.logFile = logFile
        self.sightingFile = None
        if (not(isinstance(self.logFile,str))):
           raise ValueError(functionName," logFile input is not string\n")
        if len(self.logFile) > 1:
            if (op.exists(self.logFile)):
                tempStr = self.convertMTime()
            else:
                open(self.logFile,'w').close()
                tempStr = self.convertCTime()
            with open(self.logFile,'a') as f:
                f.write("LOG:\t")
                f.write(tempStr)
                f.write(":\t")
                absPath = op.join(op.dirname(op.abspath(__file__)),self.logFile)
                f.write("Log file: ")
                f.write(absPath)
                f.write("\n")
            f.close()
        else:
           raise ValueError(functionName," logFile name is less than 2 character\n")
<<<<<<< HEAD
    
=======

>>>>>>> fef4e79... Fixed with all stars and aries file input with exception like sighting
    def setSightingFile(self,sightingFile):
        functionName = "Fix.setSightingFile:"
        self.sightingFile = sightingFile
        self.errorNo = 0
        if (not(isinstance(sightingFile,str))):
            raise ValueError(functionName," sightingFile input is not string\n")
        tmp = sightingFile.split('.')
        if len(tmp[0])  <= 1:
            raise ValueError(functionName," sightingFile length is not GE than 1\n")
        if tmp[1] !=  "xml" :
            raise ValueError(functionName," sightingFile extension is not xml\n")

<<<<<<< HEAD
        tempStr = self.convertMTime()
=======
        with open(sightingFile,'r') as f:
            try:
                tmp = f.read()
            except:
                raise IOError(functionName,"sightingFile can't be open or read")
        f.close()

>>>>>>> fef4e79... Fixed with all stars and aries file input with exception like sighting
        sightingAbsPath = op.join(op.dirname(op.abspath(__file__)),self.sightingFile)
        tmpString = self.convertMTime()
        with open(self.logFile,'a') as f:
            f.write("LOG:\t")
            f.write(tempStr)
            f.write(":\t")
            f.write("Sighting file: ")
            f.write(sightingAbsPath)
            f.write("\n")
        f.close()

        tree = ET.parse(self.sightingFile)
        root = tree.getroot()
        for child in root.findall('sighting'):

            if child.find('body') == None :
                self.errorNo += 1
                continue
            if len(child.find('body').text) ==  0 :
                self.errorNo += 1
                continue

            if child.find('date') == None :
                self.errorNo += 1
                continue

            if len(child.find('date').text) ==  0 :
                self.errorNo += 1
                continue

            if child.find('time') == None :
                self.errorNo += 1
                continue

            if len(child.find('time').text) ==  0 :
                self.errorNo += 1
                continue

            if child.find('observation') == None :
                self.errorNo += 1
                continue

            if len(child.find('observation').text) ==  0 :
                self.errorNo += 1
                continue

            tmp = child.find('observation').text
            tmp = tmp.lstrip(' ')
            tmp = tmp.rstrip(' ')
            observation = self.angle.setDegreesAndMinutes(tmp)

        container = root.findall("sighting")
        data = []
        for elem in container:
            tmp = []

            date = elem.find('date').text
            time = elem.find('time').text
            body = elem.find('body').text

            observation = elem.find('observation').text
            tmp.append(observation)

            if elem.find('height') == None:
                tmp.append(0)
            elif elem.find('height').text > 0:
                tmp.append(elem.find('height').text)
            else:
                tmp.append(0)

            if elem.find('temperature') == None:
                tmp.append(5*float(72-32)/9)
            elif elem.find('temperature').text > -20 and elem.find('temperature').text < 120:
                tmp.append(5*(float(elem.find('temperature').text)-32)/9)
            else:
                tmp.append(5*float(72-32)/9)

            if elem.find('pressure') == None:
                tmp.append(1010)
            elif elem.find('pressure').text > 100 and elem.find('temperature').text < 1100:
                tmp.append(elem.find('pressure').text)
            else:
                tmp.append(1010)

            if elem.find('horizon') == None:
                tmp.append("natural")
            else:
                tmp.append(elem.find('horizon').text)

            data.append((date,time,body,tmp))
        data.sort()

        self.sightingFileData = data

        return sightingAbsPath

    def setAriesFile(self,ariesFile="aries.txt"):
        functionName = "Fix.setAriesFile:"
        self.ariesFile = ariesFile
        ariesAbsPath = op.join(op.dirname(op.abspath(__file__)),self.ariesFile)
        if (not(isinstance(ariesFile,str))):
            raise ValueError(functionName," AriesFile input is not string\n")
        tmp = ariesFile.split('.')
        if len(tmp[0])  <= 1:
            raise ValueError(functionName," AriesFile length is not GE than 1\n")
        if tmp[1] !=  "txt" :
            raise ValueError(functionName," AriesFile extension is not txt\n")
        self.ariesData = []
        with open(ariesFile,'r') as f:
            data = csv.reader(f,delimiter='\t')
            for row in data:
                newdate = row[0]
                hh = int(row[1])
<<<<<<< HEAD
                degreeMinute = self.angle.setDegreesAndMinutes(row[2])
                self.ariesData.append(newdate,hh,degreeMinute)
=======
                degreeMinute = self.anAngle.setDegreesAndMinutes(row[2])
                self.ariesData.append((newdate,hh,degreeMinute))

        f.close()

        tmpString = self.convertMTime()
        with open(self.logFile,'a') as f:
            f.write("LOG:\t")
            f.write(tmpString)
            f.write(":\t")
            f.write("Aries file: ")
            f.write(ariesAbsPath)
            f.write("\n")
>>>>>>> fef4e79... Fixed with all stars and aries file input with exception like sighting
        f.close()

        return ariesAbsPath

    def setStarFile(self,starFile="stars.txt"):
        functionName = "Fix.setStarFile:"
        self.starFile = starFile
        starAbsPath = op.join(op.dirname(op.abspath(__file__)),self.starFile)
        if (not(isinstance(starFile,str))):
            raise ValueError(functionName," StarFile input is not string\n")
        tmp = starFile.split('.')
        if len(tmp[0])  <= 1:
            raise ValueError(functionName," StarFile length is not GE than 1\n")
        if tmp[1] !=  "txt" :
            raise ValueError(functionName," StarFile extension is not txt\n")
        self.starData = []
        with open(starFile,'r') as f:
            data = csv.reader(f,delimiter='\t')
            for row in data:
                body = row[0]
<<<<<<< HEAD
                newdate = datetime.strptime(row[1],"%m/%d/%y")
                longitudedegreeMinute = self.angle.setDegreesAndMinutes(row[2])
=======
                newdate = row[1]
                longitudedegreeMinute = self.anAngle.setDegreesAndMinutes(row[2])
>>>>>>> fef4e79... Fixed with all stars and aries file input with exception like sighting
                latitudedegreeMinute = row[3]
                self.starData.append((body,newdate,longitudedegreeMinute,latitudedegreeMinute))
        f.close()

        tmpString = self.convertMTime()
        with open(self.logFile,'a') as f:
            f.write("LOG:\t")
            f.write(tmpString)
            f.write(":\t")
            f.write("Star file: ")
            f.write(starAbsPath)
            f.write("\n")
        f.close()
        return starAbsPath

    def getSightings(self):
        functionName = "Fix.getSightings:"
        self.approximateLatitude = "0d0.0"
        self.approximateLongitude = "0d0.0"
        if (self.sightingFile == None):
            raise ValueError(functionName,"No sighting file has been set ")
        if (self.ariesFile == None):
            raise ValueError(functionName,"No aries file has been set ")
        if (self.starFile == None):
            raise ValueError(functionName,"No star file has been set ")

        tempStr = self.convertMTime()
        with open(self.logFile,'a') as f:
            for item in self.sightingFileData:
<<<<<<< HEAD
                f.write("LOG:\t")
                f.write(tempStr)
                f.write(":\t")
                f.write(item[2])
                f.write("\t")
                f.write(item[0])
                f.write("\t")
                f.write(item[1])
                f.write("\t")
=======
>>>>>>> fef4e79... Fixed with all stars and aries file input with exception like sighting

                tmp = item[3][0]
                tmp = tmp.lstrip(' ')
                tmp = tmp.rstrip(' ')

                obsevedAltitude = self.angle.setDegreesAndMinutes(tmp)
                tmpAltitude = self.angle.setDegreesAndMinutes("0d0.1")

                if obsevedAltitude < tmpAltitude:
                    raise ValueError(functionName," observerAltitude is LE 0.1 arc minute\n")

                if item[3][4] == "natural":
                    dip = (-0.97*math.sqrt(item[3][1]))/60
                else:
                    dip = 0

                refraction  = (-0.00452*item[3][3])/(273+item[3][2])/math.tan(math.radians(obsevedAltitude))

                adjustedAltitude = obsevedAltitude + dip + refraction
<<<<<<< HEAD
                string = ""
                string +=  str(int(adjustedAltitude))
                string += "d"
                string += str(round(((adjustedAltitude - int(adjustedAltitude))*60),1))
                f.write(string)
                f.write("\t")
                index = None
                lowerIndex =  None
                for i in range(len(self.starData)):
                    if self.starData[i][0] == item[2] and self.starData[i][1] == item[0] :
                        index = i
                        break
                    if self.starData[i][0] == item[2] and self.starData[i][1] < item[0] and index == None:
                        lowerIndex = i
                if index != None:
                    SHA_star = self.starData[index][2]
                    latitude = self.starData[index][3]
                else:
                    SHA_star = self.starData[lowerIndex][2]
                    latitude = self.starData[lowerIndex][3]
                    
                flag = True
                for i in range(len(self.ariesData)):
                    if self.ariesData[i][0] == item[2] and self.ariesData[i][1] == item[1].split(":")[0] and flag == True:
                        storeHour = self.ariesData[i][1] +1
                        GHA_aries1 = self.ariesData[i][3]
                        flag = False
                    if flag == False and self.ariesData[i][0] == item[2] and self.ariesData[i][1] == storeHour:
                        storeHour = self.ariesData[i][1]
                        GHA_aries2 = self.ariesData[i][3]
                GHA_aries = GHA_aries1 + math.abs(GHA_aries2 - GHA_aries1) * (int(item[1].split(":")[1])*60 + int(item[1].split(":")[2]))/3600
                longitude = SHA_star + GHA_aries
                f.write(latitude)
                f.write("\t")
                string = ""
                string +=  str(int(longitude))
                string += "d"
                string += str(round(((longitude - int(longitude))*60),1))
                f.write(string)
                f.write("\n")
=======
                adjustedString = ""
                adjustedString +=  str(int(adjustedAltitude))
                adjustedString += "d"
                adjustedString += str(round(((adjustedAltitude - int(adjustedAltitude))*60),1))
                index = None
                latitude = "0d0.0"
                longitude = 0.0

                for i in range(len(self.starData)):
                    Date = datetime.strftime(datetime.strptime(self.starData[i][1], "%m/%d/%y").date(),"%Y-%m-%d")
                    if self.starData[i][0] == item[2]:
                        if Date == item[0]:
                            index = i
                            break
                        elif Date < item[0]:
                            index = i
                if index != None:
                    flag = True
                    for i in range(len(self.ariesData)):
                        Date = datetime.strftime(datetime.strptime(self.ariesData[i][0], "%m/%d/%y").date(),"%Y-%m-%d")
                        if  Date == item[0] and int(self.ariesData[i][1]) == int(item[1].split(":")[0]) and flag == True:
                            if (int(self.ariesData[i][1]) + 1) % 24 == 0:
                                storeHour = 0
                                fixedDate = datetime.strftime((datetime.strptime(self.ariesData[i][0], "%m/%d/%y").date() + timedelta(days=1)),"%Y-%m-%d")
                            else:
                                storeHour = int(self.ariesData[i][1])+1
                                fixedDate = datetime.strftime(datetime.strptime(self.ariesData[i][0], "%m/%d/%y").date(),"%Y-%m-%d")
                            GHA_aries1 = self.ariesData[i][2]
                            flag = False
                        if flag == False and Date == fixedDate and int(self.ariesData[i][1]) == storeHour:
                            storeHour = self.ariesData[i][1]
                            GHA_aries2 = self.ariesData[i][2]
                    SHA_star = self.starData[index][2]
                    latitude = self.starData[index][3]
                    GHA_aries = GHA_aries1 + math.fabs(GHA_aries2 - GHA_aries1) * (int(item[1].split(":")[1])*60 + int(item[1].split(":")[2]))/3600
                    longitude = (SHA_star + GHA_aries) % 360
                    string = ""
                    string +=  str(int(longitude))
                    string += "d"
                    string += str(round(((longitude - int(longitude))*60),1))
                    f.write("LOG:\t")
                    tmpString = self.convertMTime()
                    f.write(tmpString)
                    f.write(":\t")
                    f.write(item[2])
                    f.write("\t")
                    f.write(item[0])
                    f.write("\t")
                    f.write(item[1])
                    f.write("\t")
                    f.write(adjustedString)
                    f.write("\t")
                    f.write(latitude)
                    f.write("\t")
                    f.write(string)
                    f.write("\n")
                else:
                    self.errorNo += 1
>>>>>>> fef4e79... Fixed with all stars and aries file input with exception like sighting

            tempStr = self.convertMTime()
            f.write("LOG:\t")
            f.write(tempStr)
            f.write(":\t")
            f.write("Sighting errors:")
            f.write(":\t")
<<<<<<< HEAD
            f.write(str(self.errnoNo))
            f.write("\n")

            tempStr = self.convertMTime()
            f.write("LOG:\t")
            f.write(tempStr)
            f.write(":\t")
            f.write("End of sighting file: ")
            f.write(self.sightingFile)
=======
            f.write(str(self.errorNo))
>>>>>>> fef4e79... Fixed with all stars and aries file input with exception like sighting
            f.write("\n")

        f.close()

        return (self.approximateLatitude,self.approximateLongitude)

    def convertCTime(self):
        ts = op.getctime(self.logFile)
        dt = datetime.fromtimestamp(ts, pytz.timezone('Etc/GMT+6'))
        return dt.isoformat(' ')

    def convertMTime(self):
        ts = op.getmtime(self.logFile)
        dt = datetime.fromtimestamp(ts, pytz.timezone('Etc/GMT+6'))
        return dt.isoformat(' ')
