from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, QTransform
from PySide6.QtCore import Qt, Signal, QSize, QPoint
from transfer_shape_ui import Ui_TransferShape  # 引入生成的UI文件中的类
from control_ui import Ui_Controller  # 引入生成的UI文件中的类
import sys
import math

class Controller(QMainWindow):
    sizeChanged = Signal(float)  # 自定义信号，用于比例改变
    angleChanged = Signal(float)  # 自定义信号，用于角度改变
    
    def __init__(self):
        super(Controller, self).__init__()
        self.ui = Ui_Controller()
        self.ui.setupUi(self)

        # 连接 lineEdit_Size 的文本变化信号到槽函数
        self.ui.lineEidt_Size.textChanged.connect(self.on_size_changed)
         # 连接 lineEdit_Angle 的文本变化信号到槽函数
        self.ui.lineEdit_Angle.textChanged.connect(self.on_angle_changed)

    def on_size_changed(self, text):
        try:
            scale = float(text)
            # print(f"Emitting sizeChanged signal with scale: {scale}")  # 调试输出
            self.sizeChanged.emit(scale)  # 发出比例改变信号
        except ValueError:
            print("Invalid input for scale")  # 调试输出
            pass  # 忽略无效的输入
        
    def on_angle_changed(self, text):
        try:
            angle = float(text)
            # print(f"Emitting angleChanged signal with angle: {angle}")  # 调试输出
            self.angleChanged.emit(angle)  # 发出角度改变信号
        except ValueError:
            print("Invalid input for angle")  # 调试输出
            pass  # 忽略无效的输入

class ChildWindowMove(QMainWindow):
    moved = Signal(QPoint)  # 自定义信号，用于窗口移动时发送位置
    resized = Signal(QSize)  # 自定义信号，用于窗口大小改变时发送尺寸

    def __init__(self):
        super(ChildWindowMove, self).__init__()
        self.setWindowTitle("Child Window")
        self.setMouseTracking(True)
        self.resizing = False

        self.label = QLabel("This is the child window", self)
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def moveEvent(self, event):
        super(ChildWindowMove, self).moveEvent(event)
        self.moved.emit(self.pos())  # 发出移动信号，传递当前位置

    def resizeEvent(self, event):
        super(ChildWindowMove, self).resizeEvent(event)
        self.resized.emit(self.size())  # 发出大小改变信号

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.resizing = True
            self.old_pos = event.globalPos()
            self.old_size = self.size()
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.resizing = False
            event.accept()

    def mouseMoveEvent(self, event):
        if self.resizing:
            delta = event.globalPos() - self.old_pos
            new_size = self.old_size + QSize(delta.x(), delta.y())
            self.resize(new_size)
            event.accept()
        else:
            super(ChildWindowMove, self).mouseMoveEvent(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_TransferShape()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        layout = QVBoxLayout(self.ui.centralwidget)
        layout.addWidget(self.image_label)

        self.ui.actionOpen.triggered.connect(self.open_image)
        self.ui.actionClose.triggered.connect(self.close)
        self.ui.actionMinimize.triggered.connect(self.showMinimized)
        self.ui.actionMove.triggered.connect(self.create_child_window)
        self.child_window = None
        self.ui.actionControl.triggered.connect(self.open_control_window)
        self.control_window = None

        self.current_scale = 1.0  # 初始化比例为1
        self.current_angle = 0.0  # 初始化角度为0
        
        self.setMinimumSize(200, 200)  # 设置主窗口的最小大小

    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.bmp)")
        if file_name:
            self.pixmap = QPixmap(file_name)  # 保存原始pixmap
            print(f"Image loaded: {file_name}")  # 调试输出
            self.update_image_size()

    def update_image_size(self):
        if hasattr(self, 'pixmap'):
            new_size = self.pixmap.size() * self.current_scale
            print(f"Updating image size to: {new_size}")  # 调试输出
            transformed_pixmap = self.pixmap.scaled(new_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            transform = QTransform().rotate(self.current_angle)
            transformed_pixmap = transformed_pixmap.transformed(transform, Qt.SmoothTransformation)
            self.image_label.setPixmap(transformed_pixmap)
            self.resize_main_window_to_image(transformed_pixmap.size())

    def resize_main_window_to_image(self, size):
        diagonal_length = math.sqrt(size.width() ** 2 + size.height() ** 2)
        print(f"Resizing main window to diagonal length: {diagonal_length}")  # 调试输出
        self.resize(diagonal_length, diagonal_length)

    def create_child_window(self):
        if self.child_window is None:
            self.child_window = ChildWindowMove()
            self.child_window.moved.connect(self.on_child_window_moved)
            self.align_child_window()
        self.child_window.resize(self.size().width() // 6, self.size().height() // 6)
        self.child_window.show()

    def align_child_window(self):
        if self.child_window:
            child_pos = self.mapToGlobal(self.rect().topRight())
            self.child_window.move(child_pos)

    def on_child_window_moved(self, pos):
        main_pos = pos - QPoint(self.width(), 0)
        self.move(main_pos)

    def open_control_window(self):
        if self.control_window is None:
            self.control_window = Controller()
            self.control_window.sizeChanged.connect(self.on_scale_changed)  # 连接信号
            self.control_window.angleChanged.connect(self.on_angle_changed)  # 连接信号
        self.control_window.show()

    def on_scale_changed(self, scale):
        print(f"Received scale change: {scale}")  # 调试输出
        self.current_scale = scale
        self.update_image_size()
    
    def on_angle_changed(self, angle):
        print(f"Received angle change: {angle}")  # 调试输出
        self.current_angle = angle
        self.update_image_size()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
