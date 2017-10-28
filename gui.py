from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(812, 690)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(812, 690))
        MainWindow.setMaximumSize(QtCore.QSize(812, 690))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(135, 0, 0, 255), stop:1 rgba(25, 10, 5, 255));\n color:rgb(255,255,255);\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.video_link_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.video_link_line_edit.setGeometry(QtCore.QRect(210, 260, 451, 31))
        self.video_link_line_edit.setStyleSheet("border:none;\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(236, 233, 230, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"Lucida Console\";\n"
"color: rgb(161, 161, 161);")
        self.video_link_line_edit.setText("")
        self.video_link_line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.video_link_line_edit.setObjectName("video_link_line_edit")
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(60, 260, 131, 31))
        self.info_label.setStyleSheet("background:none;")
        self.info_label.setObjectName("info_label")
        self.convert_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_button.setGeometry(QtCore.QRect(290, 340, 251, 51))
        self.convert_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"Impact\";\n"
"border:none;\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.0116818, x2:1, y2:0, stop:0 rgba(248, 80, 50, 255), stop:1 rgba(231, 56, 39, 255));")
        self.convert_button.setObjectName("convert_button")
        self.header_label = QtWidgets.QLabel(self.centralwidget)
        self.header_label.setGeometry(QtCore.QRect(160, 40, 501, 131))
        self.header_label.setStyleSheet("background:none;\n"
"font: 26pt \"Georgia\";\n"
"color: rgb(255, 255, 255);")
        self.header_label.setObjectName("header_label")
        self.progress = QtWidgets.QProgressBar(self.centralwidget)
        self.progress.setGeometry(QtCore.QRect(240, 450, 391, 23))
        self.progress.setStyleSheet("\n"
"QProgressBar::chunk {\n"
"   \n"
"    background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"    width: 1px;\n"
"  \n"
"};\n"
"    color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 5px;\n"
"text-align: center;\n"
"\n"
"")
        self.progress.setMinimum(0)
        self.progress.setProperty("value", 0)
        self.progress.setInvertedAppearance(False)
        self.progress.setObjectName("progress")
        self.progress_label = QtWidgets.QLabel(self.centralwidget)
        self.progress_label.setGeometry(QtCore.QRect(110, 450, 111, 21))
        self.progress_label.setStyleSheet("background:none;")
        self.progress_label.setObjectName("progress_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube 2 mp3"))
        self.info_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ebebeb;\">Youtube video link</span></p></body></html>"))
        self.convert_button.setText(_translate("MainWindow", "Convert"))
        self.header_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#ffffff;\">Youtube 2 Mp3</span></p></body></html>"))
        self.progress_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">Converting...</span></p></body></html>"))



app = QtWidgets.QApplication(sys.argv)
youtube_screen = QtWidgets.QMainWindow()
ui_youtube = Ui_MainWindow()
ui_youtube.setupUi(youtube_screen)


