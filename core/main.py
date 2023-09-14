import serial
import time
import sys
from core.qttem.QT_TEM import *
from PyQt6.QtWidgets import *


def create_data_packet(header_code, packet_len,command_code, parameter, sum):
    header_bytes = header_code.to_bytes(2, byteorder='little')
    packet_len_bytes = packet_len.to_bytes(4, byteorder='little')
    command_bytes = command_code.to_bytes(1, byteorder='little')
    parameter_bytes = parameter.to_bytes(4, byteorder='little')
    sum_bytes = sum.to_bytes(1, byteorder='little')


    data_packet = header_bytes + packet_len_bytes+ command_bytes + parameter_bytes + sum_bytes
    return data_packet

def open_ser():
    port = 'COM5'
    baudrate = 115200
    try:
        global ser
        ser = serial.Serial(port, baudrate, timeout=0.5)
        if(ser.isOpen() == True):
            print("the serial secessfully open")
    except Exception as exc:
        print("the serial fail open", exc)

def close_ser():
    try:
        global ser
        if ser.is_open:
            ser.close()
            print("Serial port closed successfully.")
        else:
            print("Serial port is not open.")
    except Exception as exc:
        print("Error while closing serial port:", exc)

def send_msg(data):
    try:
        ser.write(data)
        print("data post:", data.hex())
    except Exception as exc:
        print("post err", exc)



#
# if __name__ == '__main__':
#     header_code = 0x55AA
#     packet_len = 0x7
#     command_code = 0x01
#     parameter = 0x0
#     sum = 0x1
#     data_packet = create_data_packet(header_code, packet_len, command_code, parameter, sum)
#     while True:
#         print(data_packet)
#         open_ser()
#         send_msg(data_packet)
#         close_ser()
#         time.sleep(3)



def main():
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec())


if __name__ == '__main__':
   main()





