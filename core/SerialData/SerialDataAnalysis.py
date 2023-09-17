import serial
from core.qttem.QT_TEM import *

class SerialCommunication:
    def __init__(self):
        self.ser = None

    def open_ser(self, port, baudrate):
        try:
            global ser
            ser = serial.Serial(port, baudrate, timeout=0.5)
            if (ser.isOpen() == True):
                print("the serial secessfully open")
                print("port:", port, "Type:", type(port))
                print("baudrate:", baudrate, "Type:", type(baudrate))
        except Exception as exc:
            print("the serial fail open", exc)

    def close_ser(self):
        try:
            global ser
            if ser.is_open:
                ser.close()
                print("Serial port closed successfully.")
            else:
                print("Serial port is not open.")
        except Exception as exc:
            print("Error while closing serial port:", exc)

    def send_msg(self, data):
        try:
            ser.write(data)
            print("data post:", data.hex())
        except Exception as exc:
            print("post err", exc)

    def create_data_packet(self, header_code, packet_len, command_code, parameter, sum):
        header_bytes = header_code.to_bytes(2, byteorder='little')
        packet_len_bytes = packet_len.to_bytes(4, byteorder='little')
        command_bytes = command_code.to_bytes(1, byteorder='little')
        parameter_bytes = parameter.to_bytes(4, byteorder='little')
        sum_bytes = sum.to_bytes(1, byteorder='little')
        data_packet = header_bytes + packet_len_bytes + command_bytes + parameter_bytes + sum_bytes
        return data_packet