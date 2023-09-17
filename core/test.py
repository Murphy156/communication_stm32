import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QGraphicsView, QGraphicsScene, QGraphicsLineItem, QGraphicsTextItem, QGraphicsEllipseItem

from PyQt6.QtGui import *

class CustomGraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setScene(QGraphicsScene(self))
        self.setSceneRect(0, 0, 200, 200)

        # Create axes
        self.create_axis()

        # Add some data points
        self.add_data_points()

    def create_axis(self):
        # 创建一个 QGraphicsView
        graphics_view = QGraphicsView()

        # 设置场景
        scene = QGraphicsScene()
        graphics_view.setScene(scene)

        # 调整可视化显示的大小
        width = 200  # 根据需要调整
        height = 200  # 根据需要调整

        # 创建左侧的y轴（速度）
        y_axis = QGraphicsLineItem(0, 0, 0, height)
        y_axis.setPen(QPen(QColor("white")))
        scene.addItem(y_axis)

        # 创建x轴（时间）
        x_axis = QGraphicsLineItem(0, height / 2, width, height / 2)
        x_axis.setPen(QPen(QColor("white")))
        scene.addItem(x_axis)

        # 为x轴添加刻度线和标签
        for i in range(0, int(width) + 1, int(width / 4)):
            tick = QGraphicsLineItem(i, height / 2 - 5, i, height / 2 + 5)
            tick.setPen(QPen(QColor("white")))  # 设置刻度线颜色为白色
            scene.addItem(tick)
            label = QGraphicsTextItem(str(i))
            label.setPos(i - 10, height / 2 + 10)
            label.setDefaultTextColor(QColor("white"))
            scene.addItem(label)

        # 为y轴添加刻度线和标签
        for i in range(0, int(height) + 1, int(height / 8)):
            tick = QGraphicsLineItem(-5, i, 5, i)
            tick.setPen(QPen(QColor("white")))  # 设置刻度线颜色为白色
            scene.addItem(tick)
            label = QGraphicsTextItem(str(i))
            label.setPos(-40, i - 10)
            label.setDefaultTextColor(QColor("white"))
            scene.addItem(label)

        graphics_view.setStyleSheet("background-color: #18191c;")

        return graphics_view

    def add_data_points(self):
        # Add some data points (as ellipses) for demonstration
        data_points = [(50, 150), (100, 100), (200, 250), (300, 50)]
        for x, y in data_points:
            point = QGraphicsEllipseItem(x - 5, 200 - y - 5, 10, 10)
            point.setBrush(Qt.GlobalColor.red)
            self.scene().addItem(point)

def main():
    app = QApplication(sys.argv)
    view = CustomGraphicsView()
    view.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
