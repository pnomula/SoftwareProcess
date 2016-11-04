from datetime import datetime
from datetime import timedelta
import xml.etree.ElementTree as ET
import Navigation.prod.Angle as Angle
import sys
import os
import time
import pytz
import math
import re
import csv
class Fix:
    def __init__(self,logFile="log.txt"):
        functionName = "Fix.__init__:"
        self.angle = Angle.Angle()
        self.logFile = logFile
        self.sightingFile = None
        if (not(isinstance(self.logFile,str))):
           raise ValueError(functionName," logFile input is not string\n")
        if len(logFile) > 1:
            if (os.path.exists(self.logFile)):
                tmpString = self.convertMTime()
            else:
                open(self.logFile,'w').close()
                tmpString = self.convertCTime()
            with open(self.logFile,'a') as f:
                f.write("LOG:\t")
                f.write(tmpString)
                f.write(":\t")
                absPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),self.logFile)
                f.write("Log file: ")
                f.write(absPath)
                f.write("\n")
            f.close()
        else:
           raise ValueError(functionName," logFile name is less than 2 character\n")

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fef4e79... Fixed with all stars and aries file input with exception like sighting
=======

>>>>>>> 58cb7ca... Final Commit after merging CA03
    def setSightingFile(self,sightingFile):
=======
    def setSightingFile(self,sightingFile=None):
>>>>>>> 419e2bb... Inclueded changed CA02 TestCASE
        functionName = "Fix.setSightingFile:"
        self.sightingFile = sightingFile
        self.errorNo = 0
        if sightingFile == None:
            raise ValueError(functionName," no sightingFile is passed\n")
        if (not(isinstance(sightingFile,str))):
            raise ValueError(functionName," sightingFile input is not string\n")
        tmp = sightingFile.split('.')
        if len(tmp) == 1 :
            raise ValueError(functionName," sightingFile input is xml file with extention.\n")
        if len(tmp[0])  <= 1:
            raise ValueError(functionName," sightingFile length is not GE than 1\n")
        if tmp[1] !=  "xml" :
            raise ValueError(functionName," file extension is not xml\n")
        if os.path.exists(sightingFile):
            with open(self.sightingFile, 'r') as f:
                try:
                    tmp = f.read()
                except :
                    raise IOError(functionName,"sighingFile not able to open or read")
            f.close()
        else:
            raise IOError(functionName,"sighingFile name path is invalid")

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fef4e79... Fixed with all stars and aries file input with exception like sighting
=======
>>>>>>> 58cb7ca... Final Commit after merging CA03
        sightingAbsPath = op.join(op.dirname(op.abspath(__file__)),self.sightingFile)
=======
        sightingAbsPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),self.sightingFile)
>>>>>>> 419e2bb... Inclueded changed CA02 TestCASE
        tmpString = self.convertMTime()
        with open(self.logFile,'a') as f:
            f.write("LOG:\t")
            f.write(tmpString)
            f.write(":\t")
            f.write("Sighting file: ")
            f.write(sightingAbsPath)
            f.write("\n")
        f.close()

        tree = ET.parse(self.sightingFile)
        root = tree.getroot()
        for child in root.findall('sighting'):

            if child.find('body') == None :
                raise ValueError(functionName,"A body tag is missing")

            if child.find('body').text ==  None :
                raise ValueError(functionName,"A body text  is missing")

            tempS = child.find('body').text
            if len(tempS) == 0:
                raise ValueError(functionName,"A body text  is empty")

            if child.find('date') == None :
                raise ValueError(functionName,"A date tag is missing")

            if child.find('date').text == None :
                raise ValueError(functionName,"A date text is missing")

            tempS = child.find('date').text.split('-')
            if int(tempS[1]) >12 or int(tempS[1]) < 01 or int(tempS[2]) > 31 or int(tempS[2]) >29 and int(tempS[1]) ==02 :
                raise ValueError(functionName,"A date is invalid")

            if child.find('time') == None :
                raise ValueError(functionName,"A time tag is missing")

            if child.find('time').text ==  None :
                raise ValueError(functionName,"A time text  is missing")

            tempS = child.find('time').text.split(':')
            if len(tempS) == 1:
                raise ValueError(functionName,"A time is invalid")

            if child.find('observation') == None :
                raise ValueError(functionName,"A observation tag is missing")

            if child.find('observation').text ==  None :
                raise ValueError(functionName,"A observation text  is missing")

            tmp = child.find('observation').text
            tmp = tmp.lstrip(' ')
            tmp = tmp.rstrip(' ')
            regex = r"([-,0-9]*?[\.,0-9]*)d([0-9]*?[\.,0-9]*)"
            match = re.search(regex,tmp)
            if match == None:
                raise ValueError(functionName," a observation text is invalid")

            if child.find('temperature') != None and child.find('temperature').text != None and (int(child.find('temperature').text) < -20 or int(child.find('temperature').text) > 120 ):
                raise ValueError(functionName," a temperature text is invalid")

            if child.find('horizon') != None and child.find('horizon').text != None and ( child.find('horizon').text.lower() != 'artificial' and child.find('horizon').text.lower() != 'natural' ):
                raise ValueError(functionName," a horizon text is invalid")

            if child.find('height') != None and child.find('height').text != None and not re.match("^\d+?\.\d+?$",child.find('height').text):
                print(child.find('height').text)
                raise ValueError(functionName," a height text is invalid")

            if child.find('pressure') != None and child.find('pressure').text != None and re.match("^\d+?\.\d+?$",child.find('pressure').text):
                raise ValueError(functionName," a pressure text is invalid")

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
            elif float(elem.find('height').text) > 0:
                tmp.append(float(elem.find('height').text))
            else:
                tmp.append(0)

            if elem.find('temperature') == None:
                tmp.append(5*float(72-32)/9)
            elif int(elem.find('temperature').text) > -20 and int(elem.find('temperature').text) < 120:
                tmp.append(5*(float(elem.find('temperature').text)-32)/9)
            else:
                tmp.append(5*float(72-32)/9)

            if elem.find('pressure') == None:
                tmp.append(1010)
            elif int(elem.find('pressure').text) > 100 and int(elem.find('pressure').text) < 1100:
                tmp.append(float(elem.find('pressure').text))
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

    def setAriesFile(self,ariesFile=None):
        functionName = "Fix.setAriesFile:"
        self.ariesFile = ariesFile
        if self.ariesFile == None:
            raise ValueError(functionName," AriesFile is None\n")
        if (not(isinstance(ariesFile,str))):
            raise ValueError(functionName," AriesFile input is not string\n")
        tmp = ariesFile.split('.')
        if len(tmp) == 1 :
            raise ValueError(functionName," AriesFile file name is invalid.\n")
        if len(tmp[0])  <= 1:
            raise ValueError(functionName," AriesFile length is not GE than 1\n")
        if tmp[1] !=  "txt" :
            raise ValueError(functionName," file extension is not txt\n")
        self.ariesData = []
        if os.path.exists(ariesFile):
            with open(ariesFile,'r') as f:
                data = csv.reader(f,delimiter='\t')
                for row in data:
                    newdate = row[0]
                    hh = int(row[1])
                    degreeMinute = self.angle.setDegreesAndMinutes(row[2])
                    self.ariesData.append((newdate,hh,degreeMinute))
            f.close()
        else:
            raise IOError(functionName,"AriesFile path is invalid")

        ariesAbsPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),self.ariesFile)
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

    def setStarFile(self,starFile=None):
        functionName = "Fix.setStarFile:"
        self.starFile = starFile
        if self.starFile == None:
            raise ValueError(functionName," starFile is None\n")
        if (not(isinstance(starFile,str))):
            raise ValueError(functionName," StarFile input is not string\n")
        tmp = starFile.split('.')
        if len(tmp) == 1 :
            raise ValueError(functionName," Star File file name is invalid.\n")
        if len(tmp[0])  <= 1:
            raise ValueError(functionName," StarFile length is not GE than 1\n")
        if tmp[1] !=  "txt" :
            raise ValueError(functionName," file extension is not txt\n")
        self.starData = []
<<<<<<< HEAD
        with open(starFile,'r') as f:
            data = csv.reader(f,delimiter='\t')
            for row in data:
                body = row[0]
                newdate = row[1]
                longitudedegreeMinute = self.anAngle.setDegreesAndMinutes(row[2])
<<<<<<< HEAD
>>>>>>> fef4e79... Fixed with all stars and aries file input with exception like sighting
=======
>>>>>>> 58cb7ca... Final Commit after merging CA03
                latitudedegreeMinute = row[3]
                self.starData.append((body,newdate,longitudedegreeMinute,latitudedegreeMinute))
        f.close()

=======
        if os.path.exists(starFile):
            with open(starFile,'r') as f:
                data = csv.reader(f,delimiter='\t')
                for row in data:
                    body = row[0]
                    newdate = row[1]
                    longitudedegreeMinute = self.angle.setDegreesAndMinutes(row[2])
                    latitudedegreeMinute = row[3]
                    self.starData.append((body,newdate,longitudedegreeMinute,latitudedegreeMinute))
            f.close()
        else:
            raise IOError(functionName,"starFile path is invalid")
        starAbsPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),self.starFile)
>>>>>>> 419e2bb... Inclueded changed CA02 TestCASE
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
            raise ValueError(functionName,"no sighting file has been set ")
        if (self.ariesFile == None):
            raise ValueError(functionName,"no aries file has been set ")
        if (self.starFile == None):
            raise ValueError(functionName,"no star file has been set ")

        tmpString = self.convertMTime()
        with open(self.logFile,'a') as f:
            for item in self.sightingFileData:
<<<<<<< HEAD
                f.write("LOG:\t")
                f.write(tmpString)
                f.write(":\t")
                f.write(item[2])
                f.write("\t")
                f.write(item[0])
                f.write("\t")
                f.write(item[1])
                f.write("\t")
<<<<<<< HEAD
=======
>>>>>>> fef4e79... Fixed with all stars and aries file input with exception like sighting
=======
>>>>>>> 58cb7ca... Final Commit after merging CA03
=======
>>>>>>> 7c4ffd2... Final Commit with removed few print errors.

                tmp = item[3][0]
                tmp = tmp.lstrip(' ')
                tmp = tmp.rstrip(' ')

                obsevedAltitude = self.angle.setDegreesAndMinutes(tmp)
                tmpAltitude = self.angle.setDegreesAndMinutes("0d0.1")

                if obsevedAltitude < tmpAltitude:
                    raise ValueError(functionName," observerAltitude is LE 0.1 arc minute\n")

                if item[3][4].lower() == "natural":
                    dip = (-0.97*math.sqrt(item[3][1]))/60
                else:
                    dip = 0

                refraction  = (-0.00452*item[3][3])/(273+item[3][2])/math.tan(math.radians(obsevedAltitude))

                adjustedAltitude = obsevedAltitude + dip + refraction
<<<<<<< HEAD
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
=======
                adjustedString = ""
                adjustedString +=  str(int(adjustedAltitude))
                adjustedString += "d"
                adjustedString += str(round(((adjustedAltitude - int(adjustedAltitude))*60),1))
                index = None
                latitude = "0d0.0"
                longitude = 0.0

                for i in range(len(self.starData)):
>>>>>>> 58cb7ca... Final Commit after merging CA03
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
                    second = int(item[1].split(":")[1])*60 + int(item[1].split(":")[2])
                    GHA_aries = GHA_aries1 + float(math.fabs(GHA_aries2 - GHA_aries1) * second)/3600
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
<<<<<<< HEAD
>>>>>>> fef4e79... Fixed with all stars and aries file input with exception like sighting
=======
>>>>>>> 58cb7ca... Final Commit after merging CA03

            tmpString = self.convertMTime()
            f.write("LOG:\t")
            f.write(tmpString)
            f.write(":\t")
            f.write("Sighting errors:")
            f.write(":\t")
            f.write(str(self.errorNo))
<<<<<<< HEAD
>>>>>>> fef4e79... Fixed with all stars and aries file input with exception like sighting
=======
>>>>>>> 58cb7ca... Final Commit after merging CA03
            f.write("\n")

        f.close()

        return (self.approximateLatitude,self.approximateLongitude)

    def convertCTime(self):
        ts = os.path.getctime(self.logFile)
        dt = datetime.fromtimestamp(ts, pytz.timezone('Etc/GMT+6'))
        return dt.isoformat(' ')

    def convertMTime(self):
        ts = os.path.getmtime(self.logFile)
        dt = datetime.fromtimestamp(ts, pytz.timezone('Etc/GMT+6'))
        return dt.isoformat(' ')
