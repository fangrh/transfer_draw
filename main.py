from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, QTransform, QPainter
from PySide6.QtCore import Qt, Signal, QSize, QPoint
from transfer_shape_ui import Ui_TransferShape  # 引入生成的UI文件中的类
from control_ui import Ui_Controller  # 引入生成的UI文件中的类
import sys
import math

class Controller(QMainWindow):
    sizeChanged = Signal(float)  # Signal for size change
    angleChanged = Signal(float)  # Signal for angle change
    transparencyChanged = Signal(int)  # Signal for transparency change
    
    def __init__(self):
        super(Controller, self).__init__()
        self.ui = Ui_Controller()
        self.ui.setupUi(self)

        # Connect lineEdit_Size's textChanged signal to the slot function
        self.ui.lineEidt_Size.textChanged.connect(self.on_size_changed)
        # Connect lineEdit_Angle's textChanged signal to the slot function
        self.ui.lineEdit_Angle.textChanged.connect(self.on_angle_changed)
        # Connect QSliderTransparency's valueChanged signal to the slot function
        self.ui.QSliderTransparency.valueChanged.connect(self.on_transparency_changed)

    def on_size_changed(self, text):
        try:
            scale = float(text)
            self.sizeChanged.emit(scale)  # Emit sizeChanged signal
        except ValueError:
            pass  # Ignore invalid input
        
    def on_angle_changed(self, text):
        try:
            angle = float(text)
            self.angleChanged.emit(angle)  # Emit angleChanged signal
        except ValueError:
            pass  # Ignore invalid input

    def on_transparency_changed(self, value):
        self.transparencyChanged.emit(value)  # Emit transparencyChanged signal

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

        self.current_scale = 1.0  # Initial scale
        self.current_angle = 0.0  # Initial angle
        self.current_transparency = 255  # Initial transparency (0-255)

        self.setMinimumSize(200, 200)  # Set minimum window size

    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.bmp)")
        if file_name:
            self.pixmap = QPixmap(file_name)  # Save original pixmap
            self.update_image_size()

    def update_image_size(self):
        if hasattr(self, 'pixmap'):
            new_size = self.pixmap.size() * self.current_scale
            transformed_pixmap = self.pixmap.scaled(new_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            transform = QTransform().rotate(self.current_angle)
            transformed_pixmap = transformed_pixmap.transformed(transform, Qt.SmoothTransformation)

            # Apply transparency
            transparent_pixmap = QPixmap(transformed_pixmap.size())
            transparent_pixmap.fill(Qt.transparent)
            painter = QPainter(transparent_pixmap)
            painter.setOpacity(self.current_transparency / 255.0)
            painter.drawPixmap(0, 0, transformed_pixmap)
            painter.end()

            self.image_label.setPixmap(transparent_pixmap)
            self.resize_main_window_to_image(transformed_pixmap.size())

    def resize_main_window_to_image(self, size):
        diagonal_length = math.sqrt(size.width() ** 2 + size.height() ** 2)
        self.resize(max(200, diagonal_length), max(200, diagonal_length))

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
            self.control_window.sizeChanged.connect(self.on_scale_changed)  # Connect signal
            self.control_window.angleChanged.connect(self.on_angle_changed)  # Connect signal
            self.control_window.transparencyChanged.connect(self.on_transparency_changed)  # Connect signal
        
        # Move control window to bottom-right corner of the screen
        screen_geometry = QApplication.primaryScreen().geometry()
        control_width = self.control_window.width()
        control_height = self.control_window.height()
        control_pos = QPoint(screen_geometry.width() - control_width, screen_geometry.height() - control_height - control_height // 3)
        self.control_window.move(control_pos)
        
        self.control_window.show()

    def on_scale_changed(self, scale):
        self.current_scale = scale
        self.update_image_size()

    def on_angle_changed(self, angle):
        self.current_angle = angle
        self.update_image_size()

    def on_transparency_changed(self, transparency):
        self.current_transparency = int((transparency / 100.0) * 255)
        self.update_image_size()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
