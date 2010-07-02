import time, serial

# change these parameters to your GPS parameters
ser = serial.Serial(4)
ser.baudrate = 4800
fmt = "../data/GPS-%4d-%02d-%02d-%02d-%02d-%02d.csv"

filename = fmt % time.localtime()[:6]
f = open(filename, 'wb')
while True:
    line = ser.readline()
    f.write(line)
    print line,
