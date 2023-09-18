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
            print("Serial port is open:", ser.is_open)
            ser.write(data)
            print("data post:", data.hex())
        except Exception as exc:
            print("post err", exc)


    """
    brief:创建数据包
    para1:header_code:包头数据占两个bytes
    para2：command_code：命令数据占一个bytes
    para3：parameter：参数指令，有可能是负数，所以要对参数进行判断，占4个bytes
           这里的转换过程是：
        例子：-500（0xf4\x01\x00\x00）低字节在高位
        1、先将这个二进制数（0xf4\x01\x00\x00 = 1111 0100 0000 0001 0000 0000 0000 0000）计算反码：将所有位取反（ 0000 1011 1111 1110 1111 1111 1111 1111）
        2、在反码的基础上加1（0000 1011 1111 1110 1111 1111 1111 1111 + 1 = 0000 1011 1111 1110 1111 1111 1111 1111）
        3、将补码转换成十六进制得到'0x0b\xff\xff\xff'
        
        所以在mcu上求'0x0b\xff\xff\xff'的补码即可
        1、反码：将每一位取反得到 0xf3\x01\x00\x00
        2、补码：反码加1得到 0xf4\x01\x00\x00
        3、将 ’0xf4\x01\x00\x00‘ 转换为十进制，得到 -500。
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