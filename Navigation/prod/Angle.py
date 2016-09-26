import sys
import re
class Angle():
    def __init__(self):
        self.angle = 0.0 # set degree 0 and minute 0

    def setDegrees(self, degrees = 0.0):
        # trying to convert degree to float type,if not it will raise the exception for valueError
        try:
            degrees = float(degrees)
        except ValueError as raisedException:
            dignosticString = self.__class__.__name__ + "." + sys._getframe().f_code.co_name +  ":  \"degrees\" violates the parament specification"
            return self.angle

        # check if degree provided by user is negetive, if It is true, add with
        # 360 % to get correct degree, and dividing with 360 in case of user
        # provide degree more than 360.
        # in case of negative degree higher than 360 degree , we need to divide with -360 for geting right remainder
        if ( degrees < 1.0 ):
            self.angle = 360 + (degrees % -360)
        else:
            self.angle = degrees % 360

        return round(self.angle,1)

    def setDegreesAndMinutes(self, degrees):
        # defining the regular expression for syntax should be integer than d than float value
        regex = r"(\d+)d(\d+.\d+)"

        try:
            # if match found then right string is provide otherwise raise expection in no match found
            match = re.search(regex,degrees)
            if match is None:
                raise Exception
            else:
                # check if first group is integer object, in case of empty degree raise exception
                try:
                    self.angle = int(match.group(1))
                except:
                    raise Exception
                try:
                    # check if float is having only one decimal point, if it has more than 1 decimal point, raise exception
                    if len(match.group(2).rsplit('.')[-1]) == 1:
                        # check if float object is not negetive, minute can't be negetive, so raise execption in case of negetive
                        if float(match.group(2)) < 0.0 :
                            raise Exception
                        else:
                            # convert the minute into decimal point for storing into angle variable
                            self.angle += float(match.group(2))/60
                    else:
                        raise Exception
                except :
                    raise Exception
        except Exception as ValueError:
            Exception("{}.{}:  \"angleString\" violates the parament specification" .format(self.__class__.__name__ ,sys._getframe().f_code.co_name))
            return self.angle

        return round((float(match.group(1)) + float(match.group(2))/60),1)

    def add(self, angle):
        # check if angle is valid class object, otherwise raise exception
        try:
            if isinstance(angle,self.__class__):
                # add the other angle class object angle to called class angle
                # take modulus to take care of not crossing 360 degree
                self.angle += angle.angle
                self.angle %= 360
            else:
                raise Exception
        except Exception as ValueError:
            Exception("{}.{}:  \"angle\" is not a valid instance of Angle" .format(self.__class__.__name__ ,sys._getframe().f_code.co_name))
        return round(self.angle,1)

    def subtract(self, angle):
        # check if angle is valid class object, otherwise raise exception
        try:
            if isinstance(angle,self.__class__):
                # substract the other angle class object angle to called class angle
                # check if it is negative, then add with 360 degree
                # take modulus to take care of not crossing 360 degree
                self.angle -= angle.angle
                if self.angle < 0.0 :
                    self.angle += 360
            else:
                raise Exception
        except Exception as ValueError:
            Exception("{}.{}:  \"angle\" is not a valid instance of Angle" .format(self.__class__.__name__ ,sys._getframe().f_code.co_name))
        return round(self.angle,1)

    def compare(self, angle):
        # check if angle is valid class object, otherwise raise exception
        try:
            if isinstance(angle,self.__class__):
                # return 1 if calling class has higher angle than parameter passed angle
                if self.angle > angle.angle :
                    return 1
                # return 1 if calling class has lower angle than parameter passed angle
                elif self.angle < angle.angle:
                    return -1
                # return 0 if calling class has equal angle than parameter passed angle
                else:
                    return 0
            else:
                raise Exception
        except Exception as ValueError:
            Exception("{}.{}:  \"angle\" is not a valid instance of Angle" .format(self.__class__.__name__ ,sys._getframe().f_code.co_name))

    def getString(self):
        # convert floating point angle to convert into string as xdy.y  for angle
        string = ""
        string +=  str(int(self.angle))
        string += "d"
        string += str(round(((self.angle - int(self.angle))*60),1))
        return string

    def getDegrees(self):
        # return angle into 1 decimal point
        return round(self.angle,1)