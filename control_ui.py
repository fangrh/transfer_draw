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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGridLayout, QLabel, QPushButton, QSizePolicy,
    QSlider, QWidget)

class Ui_Controller(object):
    def setupUi(self, Controller):
        if not Controller.objectName():
            Controller.setObjectName(u"Controller")
        Controller.resize(275, 383)
        self.layoutWidget = QWidget(Controller)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 25, 252, 311))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 2)

        self.SizeSpeed = QDoubleSpinBox(self.layoutWidget)
        self.SizeSpeed.setObjectName(u"SizeSpeed")
        self.SizeSpeed.setDecimals(6)
        self.SizeSpeed.setSingleStep(0.005000000000000)
        self.SizeSpeed.setValue(0.005000000000000)

        self.gridLayout.addWidget(self.SizeSpeed, 1, 0, 1, 1)

        self.lineEdit_Size = QDoubleSpinBox(self.layoutWidget)
        self.lineEdit_Size.setObjectName(u"lineEdit_Size")
        self.lineEdit_Size.setDecimals(6)
        self.lineEdit_Size.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.lineEdit_Size, 1, 1, 1, 2)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.SizeDown = QPushButton(self.layoutWidget)
        self.SizeDown.setObjectName(u"SizeDown")

        self.gridLayout.addWidget(self.SizeDown, 2, 1, 1, 1)

        self.SizeUp = QPushButton(self.layoutWidget)
        self.SizeUp.setObjectName(u"SizeUp")

        self.gridLayout.addWidget(self.SizeUp, 2, 2, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)

        self.AngleSpeed = QDoubleSpinBox(self.layoutWidget)
        self.AngleSpeed.setObjectName(u"AngleSpeed")
        self.AngleSpeed.setDecimals(6)
        self.AngleSpeed.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.AngleSpeed, 4, 0, 1, 1)

        self.lineEdit_Angle = QDoubleSpinBox(self.layoutWidget)
        self.lineEdit_Angle.setObjectName(u"lineEdit_Angle")
        self.lineEdit_Angle.setDecimals(6)
        self.lineEdit_Angle.setMinimum(-1000.000000000000000)
        self.lineEdit_Angle.setMaximum(1000.000000000000000)
        self.lineEdit_Angle.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.lineEdit_Angle, 4, 1, 1, 2)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.AngleDown = QPushButton(self.layoutWidget)
        self.AngleDown.setObjectName(u"AngleDown")

        self.gridLayout.addWidget(self.AngleDown, 5, 1, 1, 1)

        self.AngleUp = QPushButton(self.layoutWidget)
        self.AngleUp.setObjectName(u"AngleUp")

        self.gridLayout.addWidget(self.AngleUp, 5, 2, 1, 1)

        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 6, 0, 1, 1)

        self.QCheckBoxMirror = QCheckBox(self.layoutWidget)
        self.QCheckBoxMirror.setObjectName(u"QCheckBoxMirror")
        self.QCheckBoxMirror.setChecked(False)

        self.gridLayout.addWidget(self.QCheckBoxMirror, 6, 1, 1, 1)

        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 7, 0, 1, 1)

        self.QCheckBoxOutline = QCheckBox(self.layoutWidget)
        self.QCheckBoxOutline.setObjectName(u"QCheckBoxOutline")

        self.gridLayout.addWidget(self.QCheckBoxOutline, 7, 1, 1, 1)

        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 8, 0, 1, 1)

        self.comboBoxColor = QComboBox(self.layoutWidget)
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.addItem("")
        self.comboBoxColor.setObjectName(u"comboBoxColor")

        self.gridLayout.addWidget(self.comboBoxColor, 8, 1, 1, 1)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 9, 0, 1, 1)

        self.QSlider_threshold1 = QSlider(self.layoutWidget)
        self.QSlider_threshold1.setObjectName(u"QSlider_threshold1")
        self.QSlider_threshold1.setMaximum(1000)
        self.QSlider_threshold1.setValue(50)
        self.QSlider_threshold1.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.QSlider_threshold1, 9, 1, 1, 2)

        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 10, 0, 1, 1)

        self.QSlider_threshold2 = QSlider(self.layoutWidget)
        self.QSlider_threshold2.setObjectName(u"QSlider_threshold2")
        self.QSlider_threshold2.setMaximum(1000)
        self.QSlider_threshold2.setValue(50)
        self.QSlider_threshold2.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.QSlider_threshold2, 10, 1, 1, 2)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 11, 0, 1, 1)

        self.QSliderTransparency = QSlider(self.layoutWidget)
        self.QSliderTransparency.setObjectName(u"QSliderTransparency")
        self.QSliderTransparency.setMaximum(100)
        self.QSliderTransparency.setSingleStep(1)
        self.QSliderTransparency.setValue(50)
        self.QSliderTransparency.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.QSliderTransparency, 11, 1, 1, 2)


        self.retranslateUi(Controller)

        QMetaObject.connectSlotsByName(Controller)
    # setupUi

    def retranslateUi(self, Controller):
        Controller.setWindowTitle(QCoreApplication.translate("Controller", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("Controller", u"Size speed", None))
        self.label_9.setText(QCoreApplication.translate("Controller", u"Size", None))
        self.label_10.setText(QCoreApplication.translate("Controller", u"Range 0-infity", None))
        self.SizeDown.setText(QCoreApplication.translate("Controller", u"-", None))
        self.SizeUp.setText(QCoreApplication.translate("Controller", u"+", None))
        self.label.setText(QCoreApplication.translate("Controller", u"Angle speed", None))
        self.label_2.setText(QCoreApplication.translate("Controller", u"Angle", None))
        self.label_5.setText(QCoreApplication.translate("Controller", u"Range 0-180", None))
        self.AngleDown.setText(QCoreApplication.translate("Controller", u"-", None))
        self.AngleUp.setText(QCoreApplication.translate("Controller", u"+", None))
        self.label_15.setText(QCoreApplication.translate("Controller", u"Mirror", None))
        self.QCheckBoxMirror.setText(QCoreApplication.translate("Controller", u"Enable", None))
        self.label_14.setText(QCoreApplication.translate("Controller", u"Outline", None))
        self.QCheckBoxOutline.setText(QCoreApplication.translate("Controller", u"Enable", None))
        self.label_16.setText(QCoreApplication.translate("Controller", u"Outline Color", None))
        self.comboBoxColor.setItemText(0, QCoreApplication.translate("Controller", u"White", None))
        self.comboBoxColor.setItemText(1, QCoreApplication.translate("Controller", u"Blue", None))
        self.comboBoxColor.setItemText(2, QCoreApplication.translate("Controller", u"Yellow", None))
        self.comboBoxColor.setItemText(3, QCoreApplication.translate("Controller", u"Red", None))
        self.comboBoxColor.setItemText(4, QCoreApplication.translate("Controller", u"Green", None))
        self.comboBoxColor.setItemText(5, QCoreApplication.translate("Controller", u"Gold", None))
        self.comboBoxColor.setItemText(6, QCoreApplication.translate("Controller", u"Black", None))

        self.label_12.setText(QCoreApplication.translate("Controller", u"Threshold1", None))
        self.label_13.setText(QCoreApplication.translate("Controller", u"Threshold2", None))
        self.label_11.setText(QCoreApplication.translate("Controller", u"Transparency", None))
    # retranslateUi

