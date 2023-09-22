import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, Qt
from PyQt6.QtGui import QColor

"""
   计算CRC-16校验值（生成多项式0x8005）
   :param data: 要计算CRC的数据，为bytes类型
   :return: CRC-16校验值，为整数
   """


def CalCRC_16(data1, data2, data3):

    crc = 0xFFFF
    poly = 0x8005

    # 合并数据
    if isinstance(data3, int) and data3 < 0:
        # Convert negative integers to bytes
        Data31 = data3.to_bytes(4, byteorder='little', signed=True)
    else:
        # Convert non-negative integers to bytes
        Data31 = int(data3).to_bytes(4, byteorder='little', signed=False)

    combined_data = data1.to_bytes(2, byteorder='little') + data2.to_bytes(1, byteorder='little') + Data31

    print("combined_data", combined_data)

    for i, byte in enumerate(combined_data):
        print("循环次数:", i)  # 打印循环次数
#        print("当前处理的字节:", hex(byte))  # 打印当前处理的字节
        crc ^= (byte << 8)  # 将当前字节左移8位后与CRC异或,相当于加入了对crc的影响
#        print("crc1", hex(crc))

        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ poly
#                print("crc2", hex(crc))
            else:
                crc <<= 1
#                print("crc3", hex(crc))
    return crc & 0xFFFF

if __name__ == '__main__':
    data1 = 0x55aa  # 2个字节的数据
    data2 = 0x01  # 1个字节的数据
    data3 = 0x00000064  # 4个字节的数据
    crc_result = CalCRC_16(data1, data2, data3)
    print(f"CRC-16校验值: 0x{crc_result:04X}")
