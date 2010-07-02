import serial

found = False
for i in range(64):
    try:
        ser=serial.Serial(i)
        ser.close()
        print "Found COM", i+1
        found = True
    except serial.serialutil.SerialException:
        pass

if not found:
    print "No ports found, make sure GPS is connected."
