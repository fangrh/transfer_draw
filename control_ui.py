# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'control.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSlider,
    QWidget)

class Ui_Controller(object):
    def setupUi(self, Controller):
        if not Controller.objectName():
            Controller.setObjectName(u"Controller")
        Controller.resize(313, 292)
        self.widget = QWidget(Controller)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 297, 259))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1)

        self.SizeSpeed = QLineEdit(self.widget)
        self.SizeSpeed.setObjectName(u"SizeSpeed")

        self.gridLayout.addWidget(self.SizeSpeed, 1, 0, 1, 1)

        self.lineEidt_Size = QLineEdit(self.widget)
        self.lineEidt_Size.setObjectName(u"lineEidt_Size")

        self.gridLayout.addWidget(self.lineEidt_Size, 1, 1, 1, 2)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.SizeDown = QPushButton(self.widget)
        self.SizeDown.setObjectName(u"SizeDown")

        self.gridLayout.addWidget(self.SizeDown, 2, 1, 1, 1)

        self.SizeUp = QPushButton(self.widget)
        self.SizeUp.setObjectName(u"SizeUp")

        self.gridLayout.addWidget(self.SizeUp, 2, 2, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)

        self.AngleSpeed = QLineEdit(self.widget)
        self.AngleSpeed.setObjectName(u"AngleSpeed")

        self.gridLayout.addWidget(self.AngleSpeed, 4, 0, 1, 1)

        self.lineEdit_Angle = QLineEdit(self.widget)
        self.lineEdit_Angle.setObjectName(u"lineEdit_Angle")

        self.gridLayout.addWidget(self.lineEdit_Angle, 4, 1, 1, 2)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.AngleDown = QPushButton(self.widget)
        self.AngleDown.setObjectName(u"AngleDown")

        self.gridLayout.addWidget(self.AngleDown, 5, 1, 1, 1)

        self.AngleUp = QPushButton(self.widget)
        self.AngleUp.setObjectName(u"AngleUp")

        self.gridLayout.addWidget(self.AngleUp, 5, 2, 1, 1)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 6, 0, 1, 1)

        self.OutlineEnable = QCheckBox(self.widget)
        self.OutlineEnable.setObjectName(u"OutlineEnable")

        self.gridLayout.addWidget(self.OutlineEnable, 6, 1, 1, 1)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 7, 0, 1, 1)

        self.horizontalSlider = QSlider(self.widget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setValue(50)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider, 7, 1, 1, 2)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 8, 0, 1, 1)

        self.horizontalSlider_2 = QSlider(self.widget)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setValue(50)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider_2, 8, 1, 1, 2)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)

        self.QSliderTransparency = QSlider(self.widget)
        self.QSliderTransparency.setObjectName(u"QSliderTransparency")
        self.QSliderTransparency.setMaximum(100)
        self.QSliderTransparency.setSingleStep(1)
        self.QSliderTransparency.setValue(50)
        self.QSliderTransparency.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.QSliderTransparency, 9, 1, 1, 2)


        self.retranslateUi(Controller)

        QMetaObject.connectSlotsByName(Controller)
    # setupUi

    def retranslateUi(self, Controller):
        Controller.setWindowTitle(QCoreApplication.translate("Controller", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("Controller", u"Size speed", None))
        self.label_9.setText(QCoreApplication.translate("Controller", u"Size", None))
        self.SizeSpeed.setText(QCoreApplication.translate("Controller", u"0.01", None))
        self.lineEidt_Size.setText(QCoreApplication.translate("Controller", u"1", None))
        self.label_10.setText(QCoreApplication.translate("Controller", u"Range 0-infity", None))
        self.SizeDown.setText(QCoreApplication.translate("Controller", u"-", None))
        self.SizeUp.setText(QCoreApplication.translate("Controller", u"+", None))
        self.label.setText(QCoreApplication.translate("Controller", u"Angle speed", None))
        self.label_2.setText(QCoreApplication.translate("Controller", u"Angle", None))
        self.AngleSpeed.setText(QCoreApplication.translate("Controller", u"1.0", None))
        self.lineEdit_Angle.setText(QCoreApplication.translate("Controller", u"0.0", None))
        self.label_5.setText(QCoreApplication.translate("Controller", u"Range 0-180", None))
        self.AngleDown.setText(QCoreApplication.translate("Controller", u"-", None))
        self.AngleUp.setText(QCoreApplication.translate("Controller", u"+", None))
        self.label_14.setText(QCoreApplication.translate("Controller", u"Outline", None))
        self.OutlineEnable.setText(QCoreApplication.translate("Controller", u"Enable", None))
        self.label_12.setText(QCoreApplication.translate("Controller", u"Contrast_x", None))
        self.label_13.setText(QCoreApplication.translate("Controller", u"Contrast_y", None))
        self.label_11.setText(QCoreApplication.translate("Controller", u"Transparency", None))
    # retranslateUi

