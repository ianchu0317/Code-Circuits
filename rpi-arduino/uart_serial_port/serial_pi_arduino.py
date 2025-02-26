import serial
from time import sleep

ser = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
msg = "Data to arduino\n"

sleep(3)

# Intentar abrir el puerto
#ser.open()
ser.reset_input_buffer()

print("Open Serial Port!!")

while True:
	try: 
		ser.write(msg.encode("utf-8"))
		sleep(0.01)
	except KeyboardInterrupt: 
		ser.close()
		print("Closing Serial port")
