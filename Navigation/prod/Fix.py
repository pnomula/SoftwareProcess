from datetime import datetime
import xml.etree.ElementTree as ET
import sys
import os.path
import time
import pytz
import math
import Navigation.prod.Angle as Angle
class Fix:
    def __init__(self,logFile="log.txt"):
        functionName = "Fix.__init__:"
        self.anAngle = Angle.Angle()
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
                f.write("Start of log\n")
            f.close()
        else:
           raise ValueError(functionName," logFile name is less than 2 character\n")

    def setSightingFile(self,sightingFile):
        functionName = "Fix.setSightingFile:"
        self.sightingFile = sightingFile
        if (not(isinstance(sightingFile,str))):
            raise ValueError(functionName," sightingFile input is not string\n")
        tmp = sightingFile.split('.')
        if len(tmp[0])  <= 1:
            raise ValueError(functionName," sightingFile length is not GE than 1\n")
        if tmp[1] !=  "xml" :
            raise ValueError(functionName," file extension is not xml\n")
        if os.path.exists(sightingFile):
            with open(fName, 'rb') as f:
                try:
                    tmp = f.read()
                except :
                    raise IOError(functionName,"sighingFile not able to open or read") 
            f.close()
        tmpString = self.convertMTime()
        with open(self.logFile,'a') as f:
            f.write("LOG:\t")
            f.write(tmpString)
            f.write(":\t")
            f.write("Start of sighting file: ")
            f.write(self.sightingFile)
            f.write("\n")
        f.close()

        return sightingFile 

    def getSightings(self):
        functionName = "Fix.getSightings:"
        self.approximateLatitude = "0d0.0"
        self.approximateLongitude = "0d0.0"
        if (self.sightingFile == None):
            raise ValueError(functionName,"no sighting file has been set ")
        tree = ET.parse(self.sightingFile)
        root = tree.getroot()
        for child in root.findall('sighting'):

            if child.find('body') == None :
                raise ValueError(functionName,"A body tag is missing")

            if len(child.find('body').text) ==  0 :
                raise ValueError(functionName,"A body text  is missing")

            if child.find('date') == None :
                raise ValueError(functionName,"A date tag is missing")

            if len(child.find('date').text) ==  0 :
                raise ValueError(functionName,"A date text  is missing")

            if child.find('time') == None :
                raise ValueError(functionName,"A time tag is missing")

            if len(child.find('time').text) ==  0 :
                raise ValueError(functionName,"A time text  is missing")

            if child.find('observation') == None :
                raise ValueError(functionName,"A observation tag is missing")

            if len(child.find('observation').text) ==  0 :
                raise ValueError(functionName,"A observation text  is missing")

            tmp = child.find('observation').text
            tmp = tmp.lstrip(' ')
            tmp = tmp.rstrip(' ')
            observation = self.anAngle.setDegreesAndMinutes(tmp)

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

        tmpString = self.convertMTime()
        with open(self.logFile,'a') as f:
            for item in data:
                f.write("LOG:\t")
                f.write(tmpString)
                f.write(":\t")
                f.write(item[2])
                f.write("\t")
                f.write(item[0])
                f.write("\t")
                f.write(item[1])
                f.write("\t")

                tmp = item[3][0]
                tmp = tmp.lstrip(' ')
                tmp = tmp.rstrip(' ')

                obsevedAltitude = self.anAngle.setDegreesAndMinutes(tmp)
                tmpAltitude = self.anAngle.setDegreesAndMinutes("0d0.1")

                if obsevedAltitude < tmpAltitude:
                    raise ValueError(functionName," observerAltitude is LE 0.1 arc minute\n")

                if item[3][4] == "natural":
                    dip = (-0.97*math.sqrt(item[3][1]))/60
                else:
                    dip = 0

                refraction  = (-0.00452*item[3][3])/(273+item[3][2])/math.tan(math.radians(obsevedAltitude))

                adjustedAltitude = obsevedAltitude + dip + refraction
                string = ""
                string +=  str(int(adjustedAltitude))
                string += "d"
                string += str(round(((adjustedAltitude - int(adjustedAltitude))*60),1))
                f.write(string)
                f.write("\n")
            tmpString = self.convertMTime()
            f.write("LOG:\t")
            f.write(tmpString)
            f.write(":\t")
            f.write("End of sighting file: ")
            f.write(self.sightingFile)
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
