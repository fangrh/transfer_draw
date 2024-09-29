# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transfer_shape.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_TransferShape(object):
    def setupUi(self, TransferShape):
        if not TransferShape.objectName():
            TransferShape.setObjectName(u"TransferShape")
        TransferShape.resize(608, 600)
        self.actionOpen = QAction(TransferShape)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(TransferShape)
        self.actionClose.setObjectName(u"actionClose")
        self.actionMinimize = QAction(TransferShape)
        self.actionMinimize.setObjectName(u"actionMinimize")
        self.actionMove = QAction(TransferShape)
        self.actionMove.setObjectName(u"actionMove")
        self.actionControl = QAction(TransferShape)
        self.actionControl.setObjectName(u"actionControl")
        self.actionExport = QAction(TransferShape)
        self.actionExport.setObjectName(u"actionExport")
        self.actionCut = QAction(TransferShape)
        self.actionCut.setObjectName(u"actionCut")
        self.centralwidget = QWidget(TransferShape)
        self.centralwidget.setObjectName(u"centralwidget")
        TransferShape.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TransferShape)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 608, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        TransferShape.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TransferShape)
        self.statusbar.setObjectName(u"statusbar")
        TransferShape.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionMinimize)
        self.menuFile.addAction(self.actionExport)
        self.menuTools.addAction(self.actionMove)
        self.menuTools.addAction(self.actionControl)
        self.menuTools.addAction(self.actionCut)

        self.retranslateUi(TransferShape)

        QMetaObject.connectSlotsByName(TransferShape)
    # setupUi

    def retranslateUi(self, TransferShape):
        TransferShape.setWindowTitle(QCoreApplication.translate("TransferShape", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("TransferShape", u"Open", None))
        self.actionClose.setText(QCoreApplication.translate("TransferShape", u"Close", None))
        self.actionMinimize.setText(QCoreApplication.translate("TransferShape", u"Minimize", None))
        self.actionMove.setText(QCoreApplication.translate("TransferShape", u"Move", None))
        self.actionControl.setText(QCoreApplication.translate("TransferShape", u"Control", None))
        self.actionExport.setText(QCoreApplication.translate("TransferShape", u"Export", None))
        self.actionCut.setText(QCoreApplication.translate("TransferShape", u"Cut", None))
        self.menuFile.setTitle(QCoreApplication.translate("TransferShape", u"File", None))
        self.menuTools.setTitle(QCoreApplication.translate("TransferShape", u"Tools", None))
    # retranslateUi

