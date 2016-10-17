import sys
import re
class Angle():
    def __init__(self):
        self.angle = 0.0 # set degree 0 and minute 0

    def setDegrees(self, degrees=0.0):
        functionName = "Angle.setDegrees:"
        # trying to convert degree to float type,if not it will raise the exception for valueError
        if (isinstance(degrees,str)):
            raise ValueError(functionName + "degrees given not as float")
        degrees = float(degrees)
        # check if degree provided by user is negetive, if It is true, add with
        # 360 % to get correct degree, and dividing with 360 in case of user
        # provide degree more than 360.
        # in case of negative degree higher than 360 degree , we need to divide with -360 for geting right remainder
        if ( degrees < 0.0 ):
            self.angle = 360 + (degrees % -360)
        else:
            self.angle = degrees % 360

        return self.angle

    def setDegreesAndMinutes(self, degrees):
        functionName = "Angle.setDegreesAndMinutes:"
        # defining the regular expression for syntax should be integer than d than float value
        regex = r"([-,0-9]*?[\.,0-9]*)d([0-9]*?[\.,0-9]*)"
        match = re.search(regex,degrees)
        if match == None:
            raise ValueError(functionName," \"angleString1\" violates the parament specification")
        if (match.group(1) == ""):
            raise ValueError(functionName," \"angleString5\" violates the parament specification")
        if (match.group(2) == ""):
            raise ValueError(functionName," \"angleString6\" violates the parament specification")
        if (re.search(r"\.", match.group(1))):
            raise ValueError(functionName," \"angleString2\" violates the parament specification")
        # check if float is having only one decimal point, if it has more than 1 decimal point, raise exception
        if (re.search(r"\.", match.group(2)) and len(match.group(2).rsplit('.')[-1]) > 1):
            raise ValueError(functionName," \"angleString3\" violates the parament specification")
        # check if float object is not negetive, minute can't be negetive, so raise execption in case of negetive
        if (float(match.group(2)) < 0.0) :
            raise ValueError(functionName," \"angleString4\" violates the parament specification")
        # convert the minute into decimal point for storing into angle variable
        if float(match.group(1)) < 0.0 :
            self.angle = 360 +( float(match.group(1)) % -360) - float(match.group(2))/60
        else:
            self.angle = float(match.group(1)) % 360 + float(match.group(2))/60
        return self.angle

    def add(self, angle=None):
        functionName = "Angle.add:"
        # check if angle is valid class object, otherwise raise exception
        if (angle == None):
            raise ValueError(functionName + "missing angle argument")
        if (not(isinstance(angle,self.__class__))):
            raise ValueError(functionName + "\"angle\" is not a valid instance of Angle")

        # add the other angle class object angle to called class angle
        # take modulus to take care of not crossing 360 degree
        self.angle += angle.angle
        self.angle %= 360
        return self.angle

    def subtract(self, angle=None):
        functionName = "Angle.subtract:"
        # check if angle is valid class object, otherwise raise exception
        if (angle == None):
            raise ValueError(functionName + "missing angle argument")
        if (not(isinstance(angle,self.__class__))):
            raise ValueError(functionName + "\"angle\" is not a valid instance of Angle")


        # substract the other angle class object angle to called class angle
        # check if it is negative, then add with 360 degree
        # take modulus to take care of not crossing 360 degree
        self.angle -= angle.angle
        if self.angle < 0.0 :
            self.angle += 360
        return self.angle

    def compare(self, angle=None):
        functionName = "Angle.compare:"
        # check if angle is valid class object, otherwise raise exception
        if (angle == None):
            raise ValueError(functionName + "missing angle argument")
        if (not(isinstance(angle,self.__class__))):
            raise ValueError(functionName + "\"angle\" is not a valid instance of Angle")

        # return 1 if calling class has higher angle than parameter passed angle
        if self.angle > angle.angle :
            return 1
        # return 1 if calling class has lower angle than parameter passed angle
        elif self.angle < angle.angle:
            return -1
        # return 0 if calling class has equal angle than parameter passed angle
        else:
            return 0

    def getString(self):
        # convert floating point angle to convert into string as xdy.y  for angle
        string = ""
        string +=  str(int(self.angle))
        string += "d"
        string += str(round(((self.angle - int(self.angle))*60),1))
        return string

    def getDegrees(self):
        # return angle into 1 decimal point
        return self.angle