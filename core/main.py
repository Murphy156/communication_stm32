import serial
import time
import sys
from core.qttem.QT_TEM import *
from core.SerialData.SerialDataAnalysis import *
from PyQt6.QtWidgets import *

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
#

def main():
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec())


if __name__ == '__main__':
   main()





