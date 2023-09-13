import sys
import serial
import time

port_name="/dev/ttyACM1"

if (len(sys.argv) < 2):
        print ("Put 'off' or 'forward' or 'reverse' or 'stop'")
        sys.exit(0)
else:
        direction = sys.argv[1]
print (direction)

if(direction == "off"):
  serPort = serial.Serial(port_name, 19200, timeout=1)
  relay_off = [0, 1, 2, 5, 6, 7]
  for i in relay_off:
    serPort.write(str.encode("relay off "+str(i)+"\n\r"))
  serPort.close()

if(direction == "forward"):
  serPort = serial.Serial(port_name, 19200, timeout=1)
  relay_on = [0, 1, 2]
  relay_off = [5, 6, 7]
  for i in relay_off:
    serPort.write(str.encode("relay off "+str(i)+"\n\r"))
  for i in relay_on:
    serPort.write(str.encode("relay on "+str(i)+"\n\r"))
  serPort.close()

if(direction == "reverse"):
  serPort = serial.Serial(port_name, 19200, timeout=1)
  relay_on = [0, 1, 2, 5, 6, 7]
  for i in relay_on:
    serPort.write(str.encode("relay on "+str(i)+"\n\r"))
  serPort.close()

if(direction == "stop"):
  serPort = serial.Serial(port_name, 19200, timeout=1)
  relay_on = [0, 1, 2, 5]
  relay_off = [6, 7]
  for i in relay_off:
    serPort.write(str.encode("relay off "+str(i)+"\n\r"))
  for i in relay_on:
    serPort.write(str.encode("relay on "+str(i)+"\n\r"))
  serPort.close()
