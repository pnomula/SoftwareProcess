import Navigation.prod.Angle as Angle
def main():
# ---------- constructor ----------
# Instantiate angles
    angle1 = Angle.Angle()
    angle2 = Angle.Angle()
    angle3 = Angle.Angle()
    angle4 = Angle.Angle()

# to verify the setDegrees methods for various cases
    angle1Degrees = angle1.setDegrees(9.5)        #angle1Degrees should be postive degree as 9.5
    angle2Degrees = angle2.setDegrees(degrees=-419.5)        #angle2Degrees should be negetive as higher than 360 as -419.5
    angle3Degrees = angle3.setDegrees(-19.5)        #angle3Degrees should be negetive as less than 360 as -19.5
    angle4Degrees = angle4.setDegrees(degrees="1a")        #angle4Degrees should be used as string
    print(angle1Degrees, angle2Degrees,angle3Degrees,angle4Degrees)
# to verify the setDegreesAndMinutes methods for various cases

    angle1Degrees = angle1.setDegreesAndMinutes("d10.0")   #Missing Degree Exception
    angle2Degrees = angle2.setDegreesAndMinutes("10")   #Missing Seperator Exception
    angle3Degrees = angle3.setDegreesAndMinutes("10d")   #Missing Minute Exception
    angle4Degrees = angle4.setDegreesAndMinutes("0.1d0")   #degreee must be integer
    print(angle1Degrees,angle2Degrees,angle3Degrees,angle4Degrees)

    angle1Degrees = angle1.setDegreesAndMinutes("0d-10")   #Minute can't be negetive
    angle2Degrees = angle2.setDegreesAndMinutes("0d5.44")   #Minute can't be with 2 decimal point
    angle3Degrees = angle3.setDegreesAndMinutes("xd10")   #degree should be integer
    angle4Degrees = angle4.setDegreesAndMinutes("10dy")   #minute should be float with one decimal point
    print(angle1Degrees,angle2Degrees,angle3Degrees,angle4Degrees)

    angle1Degrees = angle1.setDegreesAndMinutes("10:30")   #Missing seperator
    angle2Degrees = angle2.setDegreesAndMinutes("")   #Empty String
    angle3Degrees = angle3.setDegreesAndMinutes("45d0.0")
    angle4Degrees = angle4.setDegreesAndMinutes("0d30.0")
    print(angle1Degrees,angle2Degrees,angle3Degrees,angle4Degrees)
# ---------- add ----------
    print("Before Addition in Angle 1",angle1Degrees,angle2Degrees,angle3Degrees,angle4Degrees)
    addedDegrees1 = angle1.add(angle2)  #addedDegress1 should be 45d0 + 340d30 = 385d30 = 25d30 = 25.5
    print(addedDegrees1)
    print("After Addition in Angle1",angle1Degrees,angle2Degrees,angle3Degrees,angle4Degrees)
#### Add angle3 to angle2; save result in angle2; return result as degrees
    print("Before Addition in Angle 3",angle1Degrees,angle2Degrees,angle3Degrees,angle4Degrees)
    addedDegrees3 = angle3.add(angle2)  #addedDegrees should be 340d30 + 0d30 = 340d60 = 341d0 = 341.0
    print(addedDegrees3)
    print("After Addition in Angle3",angle1Degrees,angle2Degrees,angle3Degrees,angle4Degrees)
# should result in a ValueError exception bearing a diagnostic message.
    try:
        angle1.add("42d0")
    except ValueError as raisedException:
        diagnosticString = raisedException.args[0]
# ---------- subtract ----------
    print(angle1Degrees,angle2Degrees,angle3Degrees,angle4Degrees)
    print("Before Substration from Angle 4 to Angle 1 ",angle1Degrees,angle2Degrees,angle3Degrees,angle4Degrees)
    subtractedDegrees = angle4.subtract(angle1) #subtracted degrees should be 0d0 - 25d30 = -25d30 = 334d30= 334.5
    print("After Substration from Angle 4 to Angle 1",subtractedDegrees)
    print("Before Substration from Angle 4 to Angle 2 ",angle1Degrees,angle2Degrees,angle3Degrees,angle4Degrees)
    subtractedDegrees = angle4.subtract(angle2) #subtracted degrees should be 0d0 - 25d30 = -25d30 = 334d30= 334.5
    print("After Substration from Angle 4 to Angle 2",subtractedDegrees)
    try:
        angle1.add(0)
    except ValueError as raisedException:
        diagnosticString = raisedException.args[0]
# ---------- compare ----------
    angle1.setDegrees(45.0)
    angle2.setDegrees(45.1)
    result = angle1.compare(angle2) #result should be -1
    print(result)

    angle1.setDegrees(45.2)
    angle2.setDegrees(45.1)
    result = angle1.compare(angle2) #result should be -1
    print(result)

    angle1.setDegrees(45.0)
    angle2.setDegrees(45.0)
    result = angle1.compare(angle2) #result should be -1
    print(result)
    try:
        angle1.compare(42.0)
    except ValueError as raisedException:
        diagnosticString = raisedException.args[0]
# ---------- getString ----------
    angle1String = angle1.getString()   #angle1String should be "45d0.0"
    angle2String = angle2.getString()   #angle2String should be "45d6.0"
    angle3.setDegrees(45.123)
    angle3String = angle3.getString()   #angle3String should be "45d7.4"
    print(angle1String,angle2String,angle3String)
# ---------- getDegrees ----------
    angle1Degrees = angle1.getDegrees()   #angle1String should be 45.0
    angle2Degress = angle2.getDegrees()   #angle2String should be 45.1
    angle3Degrees = angle3.getDegrees()   #angle3String should be 45.1
    print(angle1Degrees,angle2Degress,angle3Degrees)

if __name__ == "__main__":
    main()