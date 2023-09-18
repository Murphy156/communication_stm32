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


    """
    brief:创建数据包
    para1:header_code:包头数据占两个bytes
    para2：command_code：命令数据占一个bytes
    para3：parameter：参数指令，有可能是负数，所以要对参数进行判断，占4个bytes
    para4：parity：校验位，校验1的个数
    RETURN:返回拼接的而进行数据包
    """
    def create_data_packet(self, header_code, command_code, parameter, parity):
        try:
            header_bytes = header_code.to_bytes(2, byteorder='little')
            command_bytes = command_code.to_bytes(1, byteorder='little')
            # 测试参数是否为负数
            if isinstance(parameter, int) and parameter < 0:
                # Convert negative integers to bytes
                parameter_bytes = parameter.to_bytes(4, byteorder='little', signed=True)
            else:
                # Convert non-negative integers to bytes
                parameter_bytes = int(parameter).to_bytes(4, byteorder='little', signed=False)
            parity_bytes = parity.to_bytes(1, byteorder='little')
            # for byte1 in parameter_bytes:
            #     print(f"{byte1:02x}")
            # print(parameter)
            data_packet = header_bytes + command_bytes + parameter_bytes + parity_bytes
            return data_packet
        except Exception as e:
            print("creating data err: ", str(e))