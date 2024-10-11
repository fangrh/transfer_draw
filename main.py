import cv2
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, QTransform, QImage, QPainter
from PySide6.QtCore import Qt, Signal, QSize, QPoint
from transfer_shape_ui import Ui_TransferShape
from control_ui import Ui_Controller
import sys
import math
import numpy as np

#1234

class Controller(QMainWindow):
    sizeChanged = Signal(float)
    angleChanged = Signal(float)
    cutXLeftChanged = Signal(float)
    cutXRightChanged = Signal(float)
    cutYTopChanged = Signal(float)
    cutYBottomChanged = Signal(float)
    xPositionChanged = Signal(float)
    yPositionChanged = Signal(float)
    transparencyChanged = Signal(int)
    mirrorChanged = Signal(bool)
    outlineChanged = Signal(bool)
    threshold1Changed = Signal(int)
    threshold2Changed = Signal(int)
    colorChanged = Signal(str)
    
    def __init__(self):
        super(Controller, self).__init__()
        self.ui = Ui_Controller()
        self.ui.setupUi(self)

        # Connect UI signals to the slot functions
        self.ui.lineEdit_Size.valueChanged.connect(self.on_size_changed)
        self.ui.lineEdit_Angle.valueChanged.connect(self.on_angle_changed)
        self.ui.QSliderCutXLeft.valueChanged.connect(self.on_cut_x_left_changed)
        self.ui.QSliderCutXRight.valueChanged.connect(self.on_cut_x_right_changed)
        self.ui.QSliderCutYLeft.valueChanged.connect(self.on_cut_y_top_changed)
        self.ui.QSliderCutYRight.valueChanged.connect(self.on_cut_y_bottom_changed)
        self.ui.QSliderTransparency.valueChanged.connect(self.on_transparency_changed)
        self.ui.QCheckBoxMirror.stateChanged.connect(self.on_mirror_changed)
        self.ui.QCheckBoxOutline.stateChanged.connect(self.on_outline_changed)
        self.ui.QSlider_threshold1.valueChanged.connect(self.on_threshold1_changed)
        self.ui.QSlider_threshold2.valueChanged.connect(self.on_threshold2_changed)
        self.ui.comboBoxColor.currentTextChanged.connect(self.on_color_changed)

        # Connect buttons for size adjustment
        self.ui.SizeDown.clicked.connect(self.on_size_down)
        self.ui.SizeUp.clicked.connect(self.on_size_up)
        # Connect buttons for angle adjustment
        self.ui.AngleDown.clicked.connect(self.on_angle_down)
        self.ui.AngleUp.clicked.connect(self.on_angle_up)

    def on_size_changed(self, value):
        self.sizeChanged.emit(value)

    def on_angle_changed(self, value):
        self.angleChanged.emit(value)
        
    def on_x_position_changed(self, value):
        self.xPositionChanged.emit(value)
    
    def on_y_position_changed(self, value):
        self.yPositionChanged.emit(value)
        
    def on_cut_x_left_changed(self, value):
        self.cutXLeftChanged.emit(value)
        
    def on_cut_x_right_changed(self, value):
        self.cutXRightChanged.emit(value)
        
    def on_cut_y_top_changed(self, value):
        self.cutYTopChanged.emit(value)
        
    def on_cut_y_bottom_changed(self, value):
        self.cutYBottomChanged.emit(value)

    def on_transparency_changed(self, value):
        self.transparencyChanged.emit(value)
    
    def on_mirror_changed(self, state):
        self.mirrorChanged.emit(state == 2)

    def on_outline_changed(self, state):
        self.outlineChanged.emit(state == 2)

    def on_threshold1_changed(self, value):
        self.threshold1Changed.emit(value)

    def on_threshold2_changed(self, value):
        self.threshold2Changed.emit(value)

    def on_color_changed(self, color):
        self.colorChanged.emit(color)

    def on_size_down(self):
        try:
            current_size = self.ui.lineEdit_Size.value()
            new_size = max(0.0, current_size - self.ui.SizeSpeed.value())
            self.ui.lineEdit_Size.setValue(new_size)
        except ValueError:
            pass

    def on_size_up(self):
        try:
            current_size = self.ui.lineEdit_Size.value()
            new_size = current_size + self.ui.SizeSpeed.value()
            self.ui.lineEdit_Size.setValue(new_size)
        except ValueError:
            pass

    def on_angle_down(self):
        try:
            current_angle = self.ui.lineEdit_Angle.value()
            new_angle = current_angle - self.ui.AngleSpeed.value()
            self.ui.lineEdit_Angle.setValue(new_angle)
        except ValueError:
            pass

    def on_angle_up(self):
        try:
            current_angle = self.ui.lineEdit_Angle.value()
            new_angle = current_angle + self.ui.AngleSpeed.value()
            self.ui.lineEdit_Angle.setValue(new_angle)
        except ValueError:
            pass


class ChildWindowMove(QMainWindow):
    moved = Signal(QPoint)
    resized = Signal(QSize)

    def __init__(self):
        super(ChildWindowMove, self).__init__()
        self.setWindowTitle("Moving")
        self.setMouseTracking(True)
        self.resizing = False

        self.label = QLabel("Please move this window, \n and the main window \n will move with it.", self)
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        self.setMinimumSize(200, 100)

    def moveEvent(self, event):
        super(ChildWindowMove, self).moveEvent(event)
        self.moved.emit(self.pos())

    def resizeEvent(self, event):
        super(ChildWindowMove, self).resizeEvent(event)
        self.resized.emit(self.size())

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
        self.ui.actionClose.triggered.connect(self.close_all_windows)
        self.ui.actionMinimize.triggered.connect(self.showMinimized)
        self.ui.actionMove.triggered.connect(self.create_child_window)
        self.ui.actionExport.triggered.connect(self.export_image)
        self.child_window = None
        self.ui.actionControl.triggered.connect(self.open_control_window)
        self.control_window = None

        self.current_scale = 1.0
        self.current_angle = 0.0
        self.current_x_position = 0.0
        self.current_y_position = 0.0
        self.cut_x_left = 0
        self.cut_x_right = 100
        self.cut_y_top = 0
        self.cut_y_bottom = 100
        self.current_transparency = 255
        self.mirror_enabled = False
        self.outline_enabled = False
        self.threshold1 = 100
        self.threshold2 = 200
        self.outline_color = "White"

        self.setMinimumSize(200, 200)
        self.center_main_window()
        self.create_child_window()
        self.open_control_window()

    def center_main_window(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)
    
    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.bmp *.jpeg *.gif *.tif *.tiff *.webp)")
        if file_name:
            self.pixmap = QPixmap(file_name)
            self.image = cv2.imread(file_name)
            self.update_image_size()
            
    def export_image(self):
        # 确保QApplication已经存在
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilters(["PNG files (*.png)", "JPEG files (*.jpg)", "BMP files (*.bmp)", "All files (*.*)"])
        file_dialog.setDefaultSuffix("png")
        
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            
            if file_path and self.pixmap_export:
                # 保存pixmap到文件
                image = self.pixmap_export.toImage()
                image.save(file_path)
                print(f"Image saved to {file_path}")
            else:
                print("Save operation canceled.")

    def update_image_size(self):
        if hasattr(self, 'pixmap'):
            if self.outline_enabled:
                contour_image = self.get_contour_image(self.image, self.threshold1, self.threshold2, self.outline_color)
                qimage = QImage(contour_image.data, contour_image.shape[1], contour_image.shape[0], contour_image.strides[0], QImage.Format_ARGB32)
                pixmap = QPixmap.fromImage(qimage)
            else:
                pixmap = self.pixmap
            new_size = pixmap.size() * self.current_scale
            transformed_pixmap = pixmap.scaled(new_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            transformed_pixmap = self.crop_to_window_size(transformed_pixmap)
            transform = QTransform().rotate(self.current_angle)
            if self.mirror_enabled:
                transform.scale(-1, 1)
            transformed_pixmap = transformed_pixmap.transformed(transform, Qt.SmoothTransformation)

            transparent_pixmap = QPixmap(transformed_pixmap.size())
            transparent_pixmap.fill(Qt.transparent)
            
            painter = QPainter(transparent_pixmap)
            painter.setOpacity(self.current_transparency / 255.0)
            painter.drawPixmap(0, 0, transformed_pixmap)
            painter.end()

            self.image_label.setPixmap(transparent_pixmap)
            # self.resize_main_window_to_image(transformed_pixmap.size())
            
            # 更新pixmap以用于保存
            self.pixmap_export = transparent_pixmap    
            
    def crop_to_window_size(self, pixmap):
        # Get the size of the window
        window_size = self.size()  # Assuming this is the MainWindow's size
        # Create a new pixmap for the cropped area
        cropped_pixmap = pixmap.copy(pixmap.width()*self.cut_x_left/100, pixmap.height()*self.cut_y_top/100, pixmap.width()*self.cut_x_right/100, pixmap.height()*self.cut_y_bottom/100)
        print(pixmap.width()+self.current_x_position, pixmap.height()+self.current_y_position)
        return cropped_pixmap
    
    def get_contour_image(self, image, threshold1, threshold2, color_name):
        # Resize the image
        height, width = image.shape[:2]

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, threshold1, threshold2)

        transparent_image = np.zeros((edges.shape[0], edges.shape[1], 4), dtype=np.uint8)

        color_dict = {
            "White": [255, 255, 255, 255],
            "Blue": [255, 0, 0, 255],
            "Yellow": [0, 255, 255, 255],
            "Red": [0, 0, 255, 255],
            "Green": [0, 255, 0, 255],
            "Gold": [0, 215, 255, 255],
            "Black": [0, 0, 0, 255]
        }

        color = color_dict.get(color_name, [255, 255, 255, 255])

        transparent_image[edges != 0] = color
        transparent_image[edges == 0] = [0, 0, 0, 0]

        return transparent_image

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
            self.control_window.sizeChanged.connect(self.on_scale_changed)
            self.control_window.angleChanged.connect(self.on_angle_changed)
            self.control_window.cutXLeftChanged.connect(self.on_cut_x_left_changed)
            self.control_window.cutXRightChanged.connect(self.on_cut_x_right_changed)
            self.control_window.cutYTopChanged.connect(self.on_cut_y_top_changed)
            self.control_window.cutYBottomChanged.connect(self.on_cut_y_bottom_changed)
            self.control_window.transparencyChanged.connect(self.on_transparency_changed)
            self.control_window.mirrorChanged.connect(self.on_mirror_changed)
            self.control_window.outlineChanged.connect(self.on_outline_changed)
            self.control_window.threshold1Changed.connect(self.on_threshold1_changed)
            self.control_window.threshold2Changed.connect(self.on_threshold2_changed)
            self.control_window.colorChanged.connect(self.on_color_changed)
        
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
        
    def on_cut_x_left_changed(self, cut_x_left):
        self.cut_x_left = cut_x_left
        self.update_image_size()
    
    def on_cut_x_right_changed(self, cut_x_right):
        self.cut_x_right = cut_x_right
        self.update_image_size()
    
    def on_cut_y_top_changed(self, cut_y_top):
        self.cut_y_top = cut_y_top
        self.update_image_size()
        
    def on_cut_y_bottom_changed(self, cut_y_bottom):
        self.cut_y_bottom = cut_y_bottom
        self.update_image_size()
        
        
    def on_transparency_changed(self, transparency):
        self.current_transparency = int((transparency / 100.0) * 255)
        self.update_image_size()

    def on_mirror_changed(self, enabled):
        self.mirror_enabled = enabled
        self.update_image_size()

    def on_outline_changed(self, enabled):
        self.outline_enabled = enabled
        self.update_image_size()

    def on_threshold1_changed(self, value):
        self.threshold1 = value
        if self.outline_enabled:
            self.update_image_size()

    def on_threshold2_changed(self, value):
        self.threshold2 = value
        if self.outline_enabled:
            self.update_image_size()

    def on_color_changed(self, color):
        self.outline_color = color
        if self.outline_enabled:
            self.update_image_size()

    def close_all_windows(self):
        if self.child_window:
            self.child_window.close()
        if self.control_window:
            self.control_window.close()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
