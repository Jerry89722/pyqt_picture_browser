# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogMain(object):
    def setupUi(self, DialogMain):
        DialogMain.setObjectName("DialogMain")
        DialogMain.resize(780, 615)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(DialogMain)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchLE = QtWidgets.QLineEdit(DialogMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLE.sizePolicy().hasHeightForWidth())
        self.searchLE.setSizePolicy(sizePolicy)
        self.searchLE.setObjectName("searchLE")
        self.horizontalLayout.addWidget(self.searchLE)
        self.searchPB = QtWidgets.QPushButton(DialogMain)
        self.searchPB.setObjectName("searchPB")
        self.horizontalLayout.addWidget(self.searchPB)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.nameLabel = QtWidgets.QLabel(DialogMain)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout_4.addWidget(self.nameLabel)
        self.nameInfoLabel = QtWidgets.QLabel(DialogMain)
        self.nameInfoLabel.setText("")
        self.nameInfoLabel.setObjectName("nameInfoLabel")
        self.horizontalLayout_4.addWidget(self.nameInfoLabel)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.locationLabel = QtWidgets.QLabel(DialogMain)
        self.locationLabel.setObjectName("locationLabel")
        self.horizontalLayout_3.addWidget(self.locationLabel)
        self.locationINfoLabel = QtWidgets.QLabel(DialogMain)
        self.locationINfoLabel.setText("")
        self.locationINfoLabel.setObjectName("locationINfoLabel")
        self.horizontalLayout_3.addWidget(self.locationINfoLabel)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.setStretch(0, 1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.goPB = QtWidgets.QPushButton(DialogMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goPB.sizePolicy().hasHeightForWidth())
        self.goPB.setSizePolicy(sizePolicy)
        self.goPB.setObjectName("goPB")
        self.horizontalLayout_5.addWidget(self.goPB)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previousPB = QtWidgets.QPushButton(DialogMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousPB.sizePolicy().hasHeightForWidth())
        self.previousPB.setSizePolicy(sizePolicy)
        self.previousPB.setObjectName("previousPB")
        self.horizontalLayout_2.addWidget(self.previousPB)
        self.scrollArea = QtWidgets.QScrollArea(DialogMain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 586, 506))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.contentWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.contentWidget.setObjectName("ContentWidget")
        self.contenLayout = QtWidgets.QVBoxLayout(self.contentWidget)
        self.contenLayout.setObjectName("contenLayout")
        self.verticalLayout.addWidget(self.contentWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.nextPB = QtWidgets.QPushButton(DialogMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextPB.sizePolicy().hasHeightForWidth())
        self.nextPB.setSizePolicy(sizePolicy)
        self.nextPB.setObjectName("nextPB")
        self.horizontalLayout_2.addWidget(self.nextPB)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.setStretch(2, 1)

        self.retranslateUi(DialogMain)
        QtCore.QMetaObject.connectSlotsByName(DialogMain)

    def retranslateUi(self, DialogMain):
        _translate = QtCore.QCoreApplication.translate
        DialogMain.setWindowTitle(_translate("DialogMain", "Dialog"))
        self.searchPB.setText(_translate("DialogMain", "search"))
        self.nameLabel.setText(_translate("DialogMain", "Name:"))
        self.locationLabel.setText(_translate("DialogMain", "Localtion:"))
        self.goPB.setText(_translate("DialogMain", "Go"))
        self.previousPB.setText(_translate("DialogMain", "<<"))
        self.nextPB.setText(_translate("DialogMain", ">>"))


